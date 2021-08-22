from flask import Blueprint
from flask_restful import Api

from resources import TimerResource
from resources import TimersResource

TIMER_BLUEPRINT = Blueprint("timer", __name__)

api = Api(TIMER_BLUEPRINT)

api.add_resource(TimersResource, "/timers")
api.add_resource(TimerResource, "/timer/<string:id>")
