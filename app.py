from flask import Flask, render_template, request, redirect
from forms import JobForm
from services import settings
from models import Job


app = Flask(__name__)

@app.route('/')
def index():
	form = JobForm()
	return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
