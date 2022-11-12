# Degrees website
# Made by Kush Desai
# From 3/5/2021 - 29/10/2021
# License: MIT License

'''
Repo: https://github.com/KushDesai04/13DTP-Project
'''


from flask import Flask, render_template, request, url_for
from config import Config
# from forms import FilterForm
import json


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
def home(city='christchurch'):
    return render_template('home.html', city = city)

@app.route('/get_city', methods=['POST'])
def get_city():
    city = json.loads(request.get_data())
    home(str(city))

@app.route('/get_data', methods=['POST'])
def get_data():
    data = json.loads(request.get_data())
    print(data)
    return 'a'
# @app.route('/like', methods=['POST'])
# def like():
#     degree = json.loads(request.get_data())
#     deg = models.Degree.query.filter_by(name=degree['degree']).first()
#     deg.likes += 1 if degree['positive'] else - 1
#     db.session.merge(deg)
#     db.session.commit()
#     return str(deg.likes)



if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
