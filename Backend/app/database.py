from typing import Annotated
from pydantic.functional_validators import BeforeValidator
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

USE_ATLAS = True

if USE_ATLAS:
    PyObjectId = Annotated[str, BeforeValidator(str)]

    uri = "mongodb+srv://test:test@cluster0.utigfmf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    mongodb = client.get_database('hackerton')
    collection = mongodb.get_collection('jobPosting')

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
else:
    MONGODB_URL = "mongodb://hackerton-mongo:27017/"
    client = AsyncIOMotorClient(MONGODB_URL)
    mongodb = client.get_database("hackerton")