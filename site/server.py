from bottle import route, run, view
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

@route("/")
@view("predictions")
def index():
    now = dt.now()

    x = random()

    return {
        "date": f"{now.year}-{now.month}-{now.day}",
        "predictions":generate_prophecies(),
        "special_date": x > 0.5,
        "x": x,
    }


@route("/api/test")
def api_test():
    return {"test_passed": True}


run(
    host="localhost",
    port=8080,
    autoreload=True
)
