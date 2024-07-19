from datetime import datetime
from typing import Optional

from pymongo.collection import ReturnDocument

from ...database import mongodb
from .schema import ProfileModel, ProfileCollection
collection = mongodb.get_collection("profile")

# TODO: Not Completed

async def create_profile_document(profile: ProfileModel):
    try:
        existing_profile = await collection.find_one({"userId": profile.userId})
        if not existing_profile:
            new_profile = await collection.insert_one(profile.model_dump())
            created_profile = await collection.find_one({"_id": new_profile.inserted_id})
            return ProfileModel(**created_profile)
        else:
            # profile.updatedAt = datetime.strptime(existing_profile.createdAt, "%Y-%m-%d")
            new_profile = await collection.find_one_and_replace(
                {"userId": profile.userId},
                profile.model_dump(),
                return_document=ReturnDocument.AFTER,
            )
            return ProfileModel(**new_profile)

    except Exception as e:
        print(f"Error creating profile: {e}")
        return None

async def create_profile(profile: ProfileModel):
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


async def get_profile(userId: str) -> ProfileModel:
    profile_data = collection.find_one({"userId": userId})
    if profile_data:
        return ProfileModel(**profile_data)

async def get_profiles():
    list_profiles = await collection.find().to_list(10)
    return ProfileCollection(profiles=list_profiles)
