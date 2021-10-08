from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/currency_details/<int:id>')
def currency_details(id):
    return render_template('details.html')


app.run(debug=True)  