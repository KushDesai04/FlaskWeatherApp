# Flask Weather App
# Made by Kush Desai


from flask import Flask, render_template, request, url_for, redirect, abort, Response
from config import Config
import json
import requests


app = Flask(__name__)
app.config.from_object(Config)

# Reroute when a 404 error is found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Home page
@app.route('/')
def home():
    return render_template('home.html')


# Home page

@app.route('/forecast', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if city is None:
        city = 'Christchurch'

    url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

    querystring = {"city": city}

    headers = {
        "X-RapidAPI-Key": "48b40acd60mshe95879762d1b62ep1515b9jsn0c09828c305d",
        "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = (json.loads(response.text))
    print(data)

    return render_template('home.html', title='Weather App', data=data, city=city)


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])