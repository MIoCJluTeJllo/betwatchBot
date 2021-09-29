import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))

DBHOST =  str(os.getenv("DBHOST"))
DATABASE = str(os.getenv("DATABASE"))

#POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{DBHOST}/{DATABASE}"
POSTGRES_URI = "postgres://dfaresgsvnykxo:5e217af37e9b8e773e36c6d0dd9ea25d6b5b2f07b614542aa53f961495d74c20@ec2-54-74-77-126.eu-west-1.compute.amazonaws.com:5432/d2mnu5gqc31t2m"