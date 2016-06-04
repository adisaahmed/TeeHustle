import datetime
from app import db


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
