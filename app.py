from flask import Flask, render_template, request, redirect
from forms import LoginForm
from services import settings


app = Flask(__name__)

@app.route('/')
def index():
	index = Index.query.all()
	form = LoginForm()
	if request.method == 'POST' and form.validate_on_submit():
		obj = settings.create_app(**form.data)
		flash('')
		if obj:
			return redirect(url_for(''))
	return render_template('index.html', **locals())

@admin.route('/index/delete/<int:id>', methods=['POST'])
def delete_index_view(id):
	application = App.query.get(id)
	settings.delete_index(application.id)	
	flash('Deleted')
	return redirect(url_for(''))


if __name__ == '__main__':
    app.run(debug=True)












