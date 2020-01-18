from flask import Flask , render_template,url_for
from forms import RegistrationForm , LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] ='3de8d2e324a3eae8ec2060006da088e5' 
posts = [
	{	'author': 'Marcus Aurelius',
		'title' : 'Meditations',
		'date' : '1 AD'
	},

	{	'author': 'Epictetus',
		'title' : 'Stoa',
		'date' : '2 BC'
	}


]
@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html',posts=posts,title='Flask Learning')

@app.route('/about')
def about():
     return render_template('about.html')


@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('register.html', form=form,title='Register')     


@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html',title='Login', form=form)     



if __name__=='__main__':
	app.run(debug=True)    