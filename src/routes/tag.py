from flask import Blueprint
from flask_restful import Api

from resources import TagResource
from resources import TagsResource

TAG_BLUEPRINT = Blueprint("tag", __name__)

api = Api(TAG_BLUEPRINT)

api.add_resource(TagsResource, "/tags")
api.add_resource(TagResource, "/tags/<int:id>")
