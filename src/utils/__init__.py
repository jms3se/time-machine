from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

from .bcrypt import generate_hash
from .bcrypt import check_hash
from .parse_params import parse_params
