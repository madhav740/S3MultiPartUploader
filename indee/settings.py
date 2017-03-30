import os

MIME_TYPE = os.environ.get('MIME_TYPE', "application/octet-stream")
BUCKET = "testboom"
AWS_REGION = "us-west-2"
#AWS_SECRET = os.environ.get('AWS_SECRET', "the_secret_access_key")
#Give the value of secret key for your IAM user it must have access to write into that bucket
AWS_SECRET = ""
AWS_ACCESS_KEY = "" 
DEBUG = bool(int(os.environ.get('DEBUG', 1)))
ENGINE = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
PORT = 8000
CHUNK_SIZE = 6 * 1024 * 1024  # CAREFUL! If you modify this, you have to
                              # clear the chunk database; I recommend
                              # setting it before having any real upload data
