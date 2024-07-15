
from ...database import mongodb
from .schema import ProfileModel, ProfileCollection

from ...utils.gpt import ChatGPTapi
from ...utils.recording import Recording
from ...utils.stt import OpenAIstt, ETRIstt, Googlestt


# TODO: Not Completed
def create_profile_document(text: str):
    record_path = Recording().recording_speech()
    text = ETRIstt().run_stt(record_path)

    gpt = ChatGPTapi()
    gpt.set_messages(template_type="profile", text=text)
    answer = gpt.gpt_request()


async def create_profile(
    profile: ProfileModel
) -> ProfileModel:
    collection = mongodb.get_collection("profile")
    new_profile = await collection.insert_one(
        profile.model_dump()
    )
    created_profile = await collection.find_one(
        {"_id": new_profile.inserted_id}
    )
    return created_profile


async def get_profiles():
    collection = mongodb.get_collection("profile")
    list_profiles = await collection.find().to_list(10)
    return ProfileCollection(profiles=list_profiles)
