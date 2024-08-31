from flask import Flask, render_template

app = Flask(__name__)
DEBUG = True
SECRET_KEY = 'secret key'
app.config.from_object(__name__)

@app.route('/')
def base():
    return 'Base'

@app.route('/home')
def home():
    return 'Home'

if __name__ == '__main__':
    app()
