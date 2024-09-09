from flask import Flask, render_template, url_for, request

app = Flask(__name__)
DEBUG = True
SECRET_KEY = 'secret key'
app.config.from_object(__name__)
def base():
    return render_template('base.html') 

@app.route('/victoriatechnologies/', methods=['GET'])
@app.route('/victoriatechnologies/home/, methods=['GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app(debug=True)
