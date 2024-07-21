from datetime import datetime
from typing import Optional

from pymongo.collection import ReturnDocument
from pymongo.errors import PyMongoError

from ...database import mongodb
from .schema import ProfileModel, ProfileCollection

collection = mongodb.get_collection("profile")



async def create(profile: ProfileModel):
    try:
        existing_profile = await collection.find_one({"username": profile.username})
        if not existing_profile:
            new_profile = await collection.insert_one(profile.model_dump())
            created_profile = await collection.find_one({"_id": new_profile.inserted_id})
            return ProfileModel(**created_profile)
        else:
            # profile.updatedAt = datetime.strptime(existing_profile.createdAt, "%Y-%m-%d")

            new_profile = await collection.find_one_and_update(
                {"userId": profile.username},
                {"$set": profile.model_dump()},
                return_document=ReturnDocument.AFTER,
            )
            return ProfileModel(**new_profile)

    except Exception as e:
        print(f"Error creating profile: {e}")
        return None


async def update(profile: ProfileModel):
    try:
        existing_profile = await collection.find_one({"username": profile.username})
        if not existing_profile:
            return None
        else:
            # profile.updatedAt = datetime.strptime(existing_profile.createdAt, "%Y-%m-%d")
            new_profile = await collection.find_one_and_update(
                {"userId": profile.username},
                {"$set": profile.model_dump()},
                return_document=ReturnDocument.AFTER,
            )
            return ProfileModel(**new_profile)

    except Exception as e:
        print(f"Error updating profile: {e}")
        return None

async def get(username: str):
    try:
        profile_data = await collection.find_one({"username": username})
        print(f"profile_data: {profile_data}")
        if profile_data:
            return ProfileModel(**profile_data)
        else:
            return None
    except Exception as e:
        print(f"Error find {username} profile: {e}")


async def get_all():
    list_profiles = await collection.find().to_list()
    return ProfileCollection(profiles=list_profiles)

async def delete(username: str):
    try:
        delete_result = await collection.delete_one({"username": username})
        if delete_result.deleted_count == 1:
            return 'Profile successfully deleted.'
        else:
            return 'No profile found to delete.'
    except PyMongoError as e:
        raise RuntimeError("Database error occured")
    except Exception as e:
        raise RuntimeError("Unexpected error occured")
