import os
from pathlib import Path

from flask import Flask
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))
load_dotenv(Path(__file__).with_name("api.env"), override=False)

from routes.weather_routes import weather_bp

app = Flask(__name__)

app.register_blueprint(weather_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)