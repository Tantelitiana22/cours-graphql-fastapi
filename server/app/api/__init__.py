import os
from dotenv import load_dotenv
from mongoengine import connect, disconnect

_ = load_dotenv()


def create_connection():
    connect(host=os.getenv("MONGO_CONNECTION_STRING"))


def close_connection():
    disconnect()
