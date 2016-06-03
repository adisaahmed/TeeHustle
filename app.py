from flask import Flask, render_template, request, redirect
from forms import JobForm
from services import settings
# from models import Job
# from flask.ext.sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


app = Flask(__name__)

@app.route('/')
def index():
	form = JobForm()
	return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
