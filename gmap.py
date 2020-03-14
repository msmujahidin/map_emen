'''
A Web application that shows Google Maps around schools, using
the Flask framework, and the Google Maps API.
'''

from flask import Flask, render_template, abort
app = Flask(__name__)


class School:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

schools = (
    School('Lumbung Inovasi','LINOV',   -8.5818619,116.0990933),
    School('Sumbawa', 'Sumbawa',            37.8884474, -122.1155922),
    School('JONES',   'JONES', -8.6096479,116.1049475)
)
schools_by_key = {school.key: school for school in schools}


@app.route("/")
def index():
    return render_template('index.html', schools=schools)


@app.route("/<school_code>")
def show_school(school_code):
    school = schools_by_key.get(school_code)
    if school:
        return render_template('map.html', school=school)
    else:
        abort(404)

# web: gunicorn gmap:app
# app.run(host='localhost', debug=True)
