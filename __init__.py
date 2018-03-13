# Hello, Flask!
from flask import Flask, render_template, request, redirect, url_for
from plotly.offline import plot
from plotly.graph_objs import Scatter
from markupsafe import Markup
import plotly.graph_objs as go
import requests

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    data = requests.post('http://144.122.167.229/getjp', data = 'token=;preval=666;postval=666;{"771":null}')
    date_data = requests.post('http://144.122.167.229/getjp', data='token=;preval=666;postval=666;{"701":null}')
    days_data =requests.post('http://144.122.167.229/getjp', data='token:;{"867":{"0":null}}')
    a = data.json()
    b= days_data.json()
    mon = int(a['771'][0][1])
    tue = int(a['771'][1][1])
    wed = int(a['771'][2][1])
    thu = int(a['771'][3][1])
    fri = int(a['771'][4][1])
    sat = int(a['771'][5][1])
    sun = int(a['771'][6][1])
    y=[]
    x=[]
    for i in range (0,287):
        y.append(b['867']['0'][i][1][2])
    for i in range (0,287):
        x.append(b['867']['0'][i][0])
    layout = go.Layout(title='Ayasli Ges Power Output')
    trace0 = go.Bar(x=['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'], y=[mon, tue, wed, thu, fri, sat, sun],opacity=0.6 )
    trace1 = go.Scatter(y=y, x=x)
    data = [trace0]
    data2= [trace1]
    fig = go.Figure(data=data, layout=layout)
    my_plot_div = plot(fig, output_type='div')
    layout2 = go.Layout(title='Ayasli Ges Day Values')
    fig2 =  go.Figure(data=data2, layout= layout2)
    my_plot_div2 = plot(fig2, output_type='div')
    return render_template('index.html',div_placeholder= Markup(my_plot_div), div_placeholder2= Markup(my_plot_div2))

if __name__ == '__main__':
	app.run(port=5000, debug=True)
