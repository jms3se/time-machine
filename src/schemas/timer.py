from . import ma

class TimerSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "start", "stop", "description")

timer_schema = TimerSchema()
timers_schema = TimerSchema(many=True)
