from flask import Flask, render_template, request
from forms import LoginForm


app = Flask(__name__)

@app.route('/')
def index():
	form = LoginForm()

	if request.method == 'POST':
		return'Form Posted'

	elif request.method == 'GET':
		return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
