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
    School('San Fransisco', 'San Fransisco',            37.8884474, -122.1155922),
    School('Cina',   'Cina', 31.7132242,120.2585658)
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

#web: gunicorn server:app

if __name__=='__main__':
    app.run()

#web: gunicorn server:app
#app.run(host='localhost', debug=True)
