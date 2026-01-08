from flask import Flask, request, jsonify
import random

application = Flask(__name__)

@application.route("/")
def home():
    return jsonify({"service": "Weather API", "status": "running"})

@application.route("/temperature", methods=["GET"])
def temperature():
    location = request.args.get("location", "unknown")
    temp = random.randint(-10, 40)
    return jsonify({
        "location": location,
        "temperature_celsius": temp
    })

@application.route("/wind", methods=["GET"])
def wind():
    location = request.args.get("location", "unknown")
    speed = random.randint(1, 40)
    direction = random.randint(0, 359)
    return jsonify({
        "location": location,
        "wind": f"{speed}kts at {direction:03d}deg"
    })

if __name__ == "__main__":
    application.run()
