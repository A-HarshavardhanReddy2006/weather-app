from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import requests
import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

API_KEY = os.getenv("API_KEY")

search_history = []


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "weather": None,
            "history": search_history
        }
    )


@app.post("/", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = Form(...)):

    city = city.strip().title()

    if city not in search_history:
        search_history.append(city)

    search_history[:] = search_history[-5:]


    if not API_KEY:
        weather = {
            "city": None,
            "error": "API key is missing. Check environment variables."
        }

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "weather": weather,
                "history": search_history
            }
        )


    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }


    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()

        print("STATUS:", response.status_code, flush=True)
        print("DATA:", data, flush=True)

    except Exception as e:

        print("ERROR:", e)

        weather = {
            "city": None,
            "error": "Internet connection issue"
        }

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "weather": weather,
                "history": search_history
            }
        )


    if response.status_code != 200:

        weather = {
            "city": None,
            "error": data.get(
                "message",
                "Unable to fetch weather data"
            ).title()
        }

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "weather": weather,
                "history": search_history
            }
        )


    main_weather = data["weather"][0]["main"]


    if main_weather == "Rain":
        mood = "Carry an umbrella ☔"

    elif main_weather == "Clear":
        mood = "Bright sunny day ☀️"

    elif main_weather == "Clouds":
        mood = "Cloudy atmosphere ☁️"

    elif main_weather == "Snow":
        mood = "Snowfall weather ❄️"

    else:
        mood = "Enjoy the weather 🌤️"


    weather = {

        "city": city,

        "temperature":
            round(data["main"]["temp"], 1),

        "feels_like":
            round(data["main"]["feels_like"], 1),

        "humidity":
            data["main"]["humidity"],

        "wind":
            data["wind"]["speed"],

        "description":
            data["weather"][0]["description"].title(),

        "icon":
            data["weather"][0]["icon"],

        "mood":
            mood
    }


    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "weather": weather,
            "history": search_history
        }
    )