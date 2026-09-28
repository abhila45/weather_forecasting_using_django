# Weather Forecasting Using Django

This is a weather forecasting web application built using Django. It uses the OpenWeatherMap API to get weather information for a city entered by the user.

## Live Demo

https://weather-forecasting-using-django.onrender.com

## Features

* Search weather by city name
* Displays current weather information
* Uses the OpenWeatherMap API
* Uses environment variables for API keys
* Django based backend
* Static files configured for production
* Deployed using Render

## Technologies Used

* Python
* Django
* HTML
* CSS
* OpenWeatherMap API
* Requests
* python-dotenv
* WhiteNoise
* Git
* GitHub
* Render

## Project Structure

```text
weather_forecasting_using_django/
|
|-- projectwether/
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|   `-- ...
|
|-- wetherapp/
|   |-- views.py
|   |-- urls.py
|   `-- ...
|
|-- templates/
|
|-- staticfiles/
|
|-- manage.py
|-- requirements.txt
|-- .gitignore
`-- README.md
```

## Running Locally

Clone the repository:

```bash
git clone https://github.com/abhila45/weather_forecasting_using_django.git
```

Go to the project directory:

```bash
cd weather_forecasting_using_django
```

Create a virtual environment:

```bash
python -m venv env
```

Activate the virtual environment on Windows:

```bash
env\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project directory:

```env
DJANGO_SECRET_KEY=your_django_secret_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

Run the migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

## API

The application uses the OpenWeatherMap API to retrieve weather data.

An API key is required for the application to work. The key should be stored in an environment variable and should not be added directly to the source code.

## Deployment

The application is deployed on Render.

The required environment variables are configured in the Render service settings, and the project is configured to serve Django static files in production.

## What I Learned

While building this project, I worked with:

* Django project and app structure
* Django views and URL routing
* External APIs
* API requests using Python
* Environment variables
* Static files in Django
* Git and GitHub
* Django deployment
* Render

## Future Improvements

* Add a five day weather forecast
* Add weather icons
* Add location based weather
* Add search history
* Add temperature unit selection
* Improve mobile responsiveness
* Display more weather information

## Author

Abhilasha Mohanty

GitHub: https://github.com/abhila45
