from typing import Annotated
from pydantic.functional_validators import BeforeValidator
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

USE_ATLAS = True

if USE_ATLAS:
    PyObjectId = Annotated[str, BeforeValidator(str)]

    uri = "mongodb+srv://hojune0303:NgaU1hHvIGXbV2oV@sesaccluster.z0bfjrj.mongodb.net/?retryWrites=true&w=majority&appName=SeSacCluster"

    # Create a new client and connect to the server
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    mongodb = client.get_database('SeSacDatabase')

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