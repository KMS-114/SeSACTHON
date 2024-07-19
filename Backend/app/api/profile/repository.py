from pymongo.collection import ReturnDocument

from database import mongodb
from api.profile.schema import ProfileModel, ProfileCollection
from api.user.repository import find_user

from utils.gpt import ChatGPTapi
from utils.recording import Recording
from utils.stt import OpenAIstt, ETRIstt, Googlestt


# TODO: Not Completed
def create_profile_document(text: str):
    record_path = Recording().recording_speech()
    text = ETRIstt().run_stt(record_path)

    gpt = ChatGPTapi()
    gpt.set_messages(template_type="profile", text=text)
    answer = gpt.gpt_request()


async def create_profile(profile: ProfileModel):
    collection = mongodb.get_collection("profile")
    existing_profile = await collection.find_one({"userId": profile.userId})
    print(existing_profile)

    if not existing_profile:
        new_profile = await collection.insert_one(profile.model_dump())
        created_profile = await collection.find_one({"_id": new_profile.inserted_id})
        print(created_profile)
        return created_profile
    else:
        new_profile = await collection.find_one_and_replace(
            {"userId": profile.userId},
            profile.model_dump(),
            return_document=ReturnDocument.AFTER,
        )
        return new_profile


async def get_profiles():
    collection = mongodb.get_collection("profile")
    list_profiles = await collection.find().to_list(10)
    return ProfileCollection(profiles=list_profiles)
