from passlib.context import CryptContext
from bson.objectid import ObjectId

from .schema import UserModel, UserCollection
from ...database import mongodb

collection = mongodb.get_collection("user")

pwd_contenxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(user: UserModel) -> UserModel:
    user.password = pwd_contenxt.hash(user.password)
    new_user = await collection.insert_one(
        user.model_dump(by_alias=True, exclude=["id"])
    )
    created_user = await collection.find_one({"_id": new_user.inserted_id})
    return created_user


async def find_all_users():
    list_users = await collection.find().to_list(length=10)
    return UserCollection(users=list_users)


async def find_user(user_id):
    user = await collection.find_one({"_id": ObjectId(user_id)})
    user = UserModel(**user)
    return user


async def delete_user(user_id):
    dropped_user = await find_user(user_id)
    if dropped_user:
        result = await collection.delete_one({"_id": ObjectId(user_id)})
    return dropped_user
