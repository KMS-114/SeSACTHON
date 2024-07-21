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


async def find_user(username):
    # user = await collection.find_one({"_id": ObjectId(user_id)})
    user = await collection.find_one({"username": username})
    user = UserModel(**user)
    return user


async def delete_user(username):
    dropped_user = await find_user(username)
    if dropped_user:
        result = await collection.delete_one({"username": username})
    return dropped_user