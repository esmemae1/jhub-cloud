from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"service": "Weather API", "status": "running"})

@app.route("/temperature", methods=["GET"])
def temperature():
    location = request.args.get("location", "unknown")
    temp = random.randint(-10, 40)
    return jsonify({
        "location": location,
        "temperature_celsius": temp
    })

@app.route("/wind", methods=["GET"])
def wind():
    location = request.args.get("location", "unknown")
    speed = random.randint(1, 40)
    direction = random.randint(0, 359)
    return jsonify({
        "location": location,
        "wind": f"{speed}kts at {direction:03d}deg"
    })

if __name__ == "__main__":
    app.run()
