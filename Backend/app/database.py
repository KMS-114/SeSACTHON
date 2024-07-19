from typing import Annotated

from pydantic.functional_validators import BeforeValidator
from motor.motor_asyncio import AsyncIOMotorClient


MONGODB_URL = "mongodb://hackerton-mongo:27017/"
client = AsyncIOMotorClient(MONGODB_URL)
mongodb = client.get_database("hackerton")

PyObjectId = Annotated[str, BeforeValidator(str)]