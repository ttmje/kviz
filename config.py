import os
from dotenv import load_dotenv
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
admin_id = os.getenv("admin_id")
USER = os.getenv("postgres")
PASSWORD = os.getenv("123")
HOST = os.getenv("localhost")
PORT = os.getenv("5432")
DATABASE = os.getenv("ttm")