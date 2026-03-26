import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
  DB_HOST = "localhost"
  DB_NAME = "ecommerce_db"
  DB_USER = "postgres"
  DB_PASSWORD = os.getenv("DB_PASSWORD")

  FILE_PATH = "data.csv"