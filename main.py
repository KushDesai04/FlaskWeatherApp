# Degrees website
# Made by Kush Desai
# From 3/5/2021 - 29/10/2021
# License: MIT License

'''
Repo: https://github.com/KushDesai04/13DTP-Project
'''


from flask import Flask, render_template, request, url_for, redirect, abort, Response
from config import Config
# from forms import FilterForm
import json
import urllib
import requests


app = Flask(__name__)
app.config.from_object(Config)


# Sends info to every page but is used in nav
@app.context_processor
def context_processor():
    return dict(unis='a')


# Reroute when a 404 error is found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# Home page
@app.route('/')
def home():
    return render_template('home.html')


# Home page
@app.route('/<string:city>')
def forecast(city):
    return render_template('home.html', city = city)


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



'''
params = {
    #     'X-RapidAPI-Key': '48b40acd60mshe95879762d1b62ep1515b9jsn0c09828c305d',
    #     'X-RapidAPI-Host': 'weather-by-api-ninjas.p.rapidapi.com'
    # }
    # r = requests.get(
    # 'https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city=christchurch',
    # params=params)
    # data = r.text
    # print(json.loads(data))
    # '''