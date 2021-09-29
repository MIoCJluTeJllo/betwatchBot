import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))

DBHOST =  str(os.getenv("DBHOST"))
DATABASE = str(os.getenv("DATABASE"))

#POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{DBHOST}/{DATABASE}"
POSTGRES_URI = "postgres://brayggjzcoaaaw:85cd98d2e45702185f02e46ada31f43243d1563e0d6176ec26f456cc93911f07@ec2-54-74-156-137.eu-west-1.compute.amazonaws.com:5432/d5srkl8m3br4og"