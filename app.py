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


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(150), nullable=False)
    mobile_or_name_website = db.Column(db.String, nullable=False)
    describe_purpose = db.Column(db.String, nullable=False)
    website_design = db.Column(db.String, nullable=False)
    project_budget = db.Column(db.Text, nullable=False)
    project_deadline = db.Column(db.String, nullable=False)
    your_name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.Text, nullable=False)
    email_address = db.Column(db.String, nullable=False)
    finished_project = db.Column(db.String(150), unique=True)

    def __repr__(self):
        return '<Job %r>' % self.name


def populate_object(obj, ignored=[], **kwargs):
    """ populate properties on the object 'obj' based on its match in dictionary kwargs
    """
    for element in kwargs.keys():
        if element in ignored:
            kwargs.pop(element)

    for name, value in kwargs.items():
        if hasattr(obj, name):
            setattr(obj, name, value)

    return obj


def create_request(ignored_args=["id"], **kwargs):
    """ create job request
    """
    job_request = Job()
    job_request = populate_object(job_request, ignored_args, **kwargs)

    db.session.add(job_request)
    db.session.commit()

    return job_request


def delete_request(request_id):
    """ Delete job request
    """
    job_request = Job.query.get(request_id)

    if not job_request:
        raise Exception("Job Request not Found")

    try:
        db.session.delete(job_request)
    except Exception as e:
        db.session.rollback()
        print e


# setting up application views
@app.route('/', methods=["GET", "POST"])
def index():
    form = JobForm()
    if request.method == "POST" and form.validate_on_submit():
        obj = create_request(**form.data)
        flash('Application has been added successfully')
        if obj:
            return redirect(url_for('content_list'))
    return render_template('index.html', **locals())

    print "+++++", form.errors


@app.route('/index/content_list')
def content_list():
    job_request = Job.query.all()
    return render_template('content_list.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/index/delete/<int:id>', methods=['POST'])
def delete_index_view(id):
    job_request = Job.query.get(id)
    delete_index(job_request.id) 
    flash('Deleted')
    return redirect(url_for('content_list'))