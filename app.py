from flask import Flask,render_template,Response
from  fetch_pred import get_pred_eth,get_pred_btc
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from PIL import Image

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/currency_details/<int:id>')
def currency_details(id):
    if id==1:
        fig = get_pred_btc()
        fig.get_figure().savefig('static/btc-pred.png')
        return render_template('details.html' , img =1)
    elif id==3:
        fig =get_pred_eth()
        fig.get_figure().savefig('static/eth-pred.png')
        return render_template('details.html' , img =3)
    else:
       return "Model not build yet"


app.run(debug=True)  