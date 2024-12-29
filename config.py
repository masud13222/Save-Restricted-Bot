import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5767231785:AAHaszuB2epfI9oe9bLwgM8x5vpqMn5tmYA")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "5587539"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8670b598fef377e6782429b1f664dce6")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1826754085"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://cinemazbd:A3cyYdaS3JkOGYog@cluster0.akey0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))

# Verification duration in seconds (e.g., 6 hours = 21600 seconds)
VERIFICATION_DURATION = int(os.environ.get("VERIFICATION_DURATION", 21600))

# Admins who don't need verification
ADMIN_IDS = list(map(int, os.environ.get("ADMIN_IDS", "1826754085").split(',')))
