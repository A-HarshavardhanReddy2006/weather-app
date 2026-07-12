# 🌦️ Weather App

A modern weather web application built using **FastAPI**, **HTML**, **CSS**, and the **OpenWeatherMap API**.

## 🚀 Features

- 🌍 Search weather by city name
- 🌡️ Real-time temperature
- 🤗 Feels-like temperature
- 💧 Humidity
- 🌬️ Wind speed
- ☁️ Weather description
- 😊 Weather mood suggestion
- 🕒 Recent search history
- ❌ Error handling for invalid city names
- 📱 Responsive user interface

## 🛠️ Technologies Used

- Python
- FastAPI
- HTML5
- CSS3
- Jinja2 Templates
- OpenWeatherMap API
- Requests
- Python-dotenv

---

# 📸 Screenshots

## 🏠 Home Page

![Home](screenshots/home.jpeg)

---

## 🌤️ Weather Result

![Weather](screenshots/weather.jpeg)

---

## ❌ Invalid City Name

![Invalid City](screenshots/invalidCityname.jpeg)

---

## 🕒 Recent Search History

![History](screenshots/history.jpeg)

---

# 📂 Project Structure

```text
weather_project/
│
├── screenshots/
│   ├── home.jpeg
│   ├── weather.jpeg
│   ├── invalidCityname.jpeg
│   └── history.jpeg
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env (ignored)
```

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/A-HarshavardhanReddy2006/weather-app.git
```

Move into the project:

```bash
cd weather-app
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
API_KEY=YOUR_OPENWEATHER_API_KEY
```

Run the application:

```bash
uvicorn main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

# 📚 What I Learned

- FastAPI fundamentals
- Routing and form handling
- Jinja2 templates
- Working with REST APIs
- Environment variables using `.env`
- Git and GitHub
- Responsive UI development

---

# 👨‍💻 Author

**Appi Reddigari Harshavardhan Reddy**

GitHub: **https://github.com/A-HarshavardhanReddy2006**