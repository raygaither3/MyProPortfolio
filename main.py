from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
            


app = Flask(__name__)


bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)