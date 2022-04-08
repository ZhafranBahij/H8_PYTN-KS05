from flask import Flask
from markupsafe import escape
from flask import request

app = Flask(__name__)

# @app.route("/")
# def index():
#   return 'Index Page'

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user/<username>")
def show_user_profile(username):
  return 'User %s' % escape(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
  return 'Post %d' % post_id

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
  return 'Path %s' % escape(subpath)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    return do_the_login()
  else :
    return show_the_login_form()

def do_the_login():
  return 'request.method == POST, so do the login()'

def show_the_login_form():
  return 'request.method == GET, so show the login form()'

from flask import render_template

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
  return render_template('hello.html', name=name)