from .schema import UserModel, UserCollection
from ...database import mongodb


async def create_user(user: UserModel) -> UserModel:
    collection = mongodb.get_collection("user")
    new_user = await collection.insert_one(
        user.model_dump(by_alias=True, exclude=["id"])
    )
    created_user = await collection.find_one({"_id": new_user.inserted_id})
    return created_user


async def get_users():
    collection = mongodb.get_collection("user")
    list_users = await collection.find().to_list(length=10)
    return UserCollection(users=list_users)
