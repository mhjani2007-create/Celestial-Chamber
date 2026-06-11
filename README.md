# Weather App

A Flask-based weather application that provides real-time weather information.

## Features
- Real-time weather data
- Location-based forecasts
- Clean and responsive UI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mhjani2007-create/Celestial-Chamber.git
cd weather_app
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

5. Run the application:
```bash
python app.py
```

The app will be available at `http://localhost:5000`

## Deployment on Render

1. Push your code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com)
3. Click "New +" and select "Web Service"
4. Connect your GitHub repository
5. Configure the following:
   - **Name**: weather-app
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Add environment variables in the Render dashboard
7. Click "Deploy"

## Environment Variables

See `.env.example` for required environment variables.

## Technologies
- Flask
- Python
- HTML/CSS/JavaScript
