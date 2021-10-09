from flask import Flask,render_template,Response
from btc_model import get_pred
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/currency_details/<int:id>')
def currency_details(id):
    fig = get_pred()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
    # return render_template('details.html')


app.run(debug=True)  