from flask import Flask, render_template, request, redirect
from forms import LoginForm
from services import settings


app = Flask(__name__)

@app.route('/')
def index():
	apps = Index.query.all()
	form = LoginForm()
	return render_template('index.html', **locals())

@app.route('/apps/create/', methods=['POST', 'GET'])
def create_app_view():
	form = CreateLoginForm()
	if request.method == 'POST' and form.validate_on_submit():
		obj = settings.create_app(**form.data)
		flash('Application has been added successfully')
		if obj:
			return redirect(url_for(''))
	return render_template('index.html', **locals())

@app.route('/apps/update/<int:id>', methods=['POST', 'GET'])
def update_app_view(id):
	application = App.query.get(id)
	form = LoginForm(obj=application)
	if request.method == 'POST' and form.validate_on_submit():
		obj = settings.update_app(application.id, **form.data)
		print obj.name
		flash('Application has been updated successfully')
		if obj:
			return redirect(url_for(''))
	return render_template('index.html', **locals())

@app.route('/index/delete/<int:id>', methods=['POST'])
def delete_index_view(id):
	application = App.query.get(id)
	settings.delete_index(application.id)	
	flash('Deleted')
	return redirect(url_for(''))


if __name__ == '__main__':
    app.run(debug=True)
