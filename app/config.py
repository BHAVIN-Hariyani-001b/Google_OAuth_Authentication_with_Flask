from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    AUTH_URI = os.getenv("AUTH_URI")
    TOKEN_URI = os.getenv("TOKEN_URI")
    REDIRECT_URI = os.getenv("REDIRECT_URI")
