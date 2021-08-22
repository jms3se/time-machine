from flask import Blueprint
from flask_restful import Api

from resources import TimerResource
from resources import TimersResource
from resources import TimerTagResource
from resources import TimerTagsResource

TIMER_BLUEPRINT = Blueprint("timer", __name__)

api = Api(TIMER_BLUEPRINT)

api.add_resource(TimersResource, "/timers")
api.add_resource(TimerResource, "/timers/<int:id>")
api.add_resource(TimerTagsResource, "/timers/<int:id>/tags")
api.add_resource(TimerTagResource, "/timers/<int:id>/tags/<int:tag_id>")
