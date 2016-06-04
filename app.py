# import core python modules
import datetime

# import flask and its extensions
from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# import application modules
import config
from forms import JobForm
from services import settings

# initializing flask application and database
app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(config)


# setting up model objects
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    your_name = db.Column(db.String(150), nullable=False)
    project_name = db.Column(db.String, nullable=False)
    describe_purpose = db.Column(db.String, nullable=False)
    website_design = db.Column(db.String, nullable=False)
    project_budget = db.Column(db.Text, nullable=False)
    project_deadline = db.Column(db.String, nullable=False)
    finished_project = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.Text, nullable=False)
    mobile_or_name_website = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String(150), unique=True)

    def __repr__(self):
        return '<Job %r>' % self.name


# setting up application views
@app.route('/')
def index():
    form = JobForm()
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
