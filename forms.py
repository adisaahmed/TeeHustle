from flask.ext.wtf import Form
from wtforms.validators import DataRequired
from wtforms import *
from wtforms.fields.html5 import EmailField


class LoginForm(Form):
    project_name = StringField("To get us started, let's give your project a name", validators=[DataRequired()], description="test")
    mobile_or_name_website = TextField("Is it a Mobile App or Website", validators=[DataRequired()])
    describe_purpose = TextAreaField("Please describe the purpose of this project", validators=[DataRequired()])  
    website_design = TextField("Are there any website with design that you like", validators=[DataRequired()])  
    project_budget = IntegerField("What is the budget of this project", validators=[DataRequired()])  
    project_deadline = StringField("What is the deadline for this project?", validators=[DataRequired()])  
    your_name = StringField("What is your name?", validators=[DataRequired()])  
    phone_number = IntegerField("What is your phone number?", validators=[DataRequired()])  
    email_address = EmailField('What is your email address?', validators=[DataRequired()])
    finished_project = TextAreaField('Describe how you envision the finished project', validators=[DataRequired()])