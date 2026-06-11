from flask import Blueprint, render_template, request
from services.weather_service import get_weather

weather_bp = Blueprint("weather", __name__)


@weather_bp.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if city:
            weather = get_weather(city)
            if weather is None:
                error = "Weather data could not be loaded. Please try again."

    return render_template("index.html", weather=weather, error=error)