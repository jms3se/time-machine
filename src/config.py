import logging
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "DEV")
DEBUG = ENVIRONMENT == "DEV"
APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "/api")
HOST = os.getenv("APPLICATION_HOST", "127.0.0.1")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv("SECRET_KEY", "epanenem")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "epanenem")
JWT_BLACKLIST_ENABLED = os.getenv("JWT_BLACKLIST_ENABLED", True)
JWT_BLACKLIST_TOKEN_CHECKS = os.getenv("JWT_BLACKLIST_TOKEN_CHECKS", ['access', 'refresh'])

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_DB = os.getenv("REDIS_DB", 0)
REDIS_DECODE_RESPONSES = os.getenv("REDIS_DECODE_RESPONSES", True)

SENTRY_DNS = os.getenv("SENTRY_KEY", "https://b963fa126e6e48bc8623a727adaf7591@o288279.ingest.sentry.io/5920314")

DB_CONTAINER = os.getenv("APPLICATION_DB_CONTAINER", "localhost")
POSTGRES = {
    "user": os.getenv("APPLICATION_POSTGRES_USER", "postgres"),
    "pw": os.getenv("APPLICATION_POSTGRES_PW", "postgres"),
    "host": os.getenv("APPLICATION_POSTGRES_HOST", "localhost"),
    "port": os.getenv("APPLICATION_POSTGRES_PORT", 5432),
    "db": os.getenv("APPLICATION_POSTGRES_DB", "postgres"),
}
DB_URI = "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
