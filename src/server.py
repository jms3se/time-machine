from flask import Flask
from flask.blueprints import Blueprint
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

import config
import routes
from models import db
from repositories import BlocklistRepository

server = Flask(__name__)

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
server.config["SECRET_KEY"] = config.SECRET_KEY
server.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
server.config['JWT_BLACKLIST_ENABLED'] = config.JWT_BLACKLIST_ENABLED
server.config['JWT_BLACKLIST_TOKEN_CHECKS'] = config.JWT_BLACKLIST_TOKEN_CHECKS

db.init_app(server)
db.app = server
migrate = Migrate(server, db)
jwt = JWTManager(server)

CORS(server, resources={r"/api/*": {"origins": "*"}})

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token_in_redis = BlocklistRepository.get(jti)
    return token_in_redis is not None

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

if __name__ == "__main__":
    server.run(debug=True, host=config.HOST, port=config.PORT)
