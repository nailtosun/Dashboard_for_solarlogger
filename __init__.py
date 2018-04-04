# Hello, Flask!
from flask import Flask, render_template, request, redirect, url_for
from plotly.offline import plot
from plotly.graph_objs import Scatter
from markupsafe import Markup
import plotly.graph_objs as go
import requests
import pandas as pd

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    data = requests.post('http://144.122.167.229/getjp', data = 'token=;preval=666;postval=666;{"771":null}')
    date_data = requests.post('http://144.122.167.229/getjp', data='token=;preval=666;postval=666;{"701":null}')
    days_data =requests.post('http://144.122.167.229/getjp', data='token:;{"867":{"0":null}}')
    total_power=requests.post('http://144.122.167.229/getjp', data='token:;preval=none;{"801":{"130":null,"131":null,"132":null,"133":null,"134":null}}')
    current_power=requests.post('http://144.122.167.229/getjp', data = 'token: ;{"780":null,"781":null,"858":null,"862":null,"863":null}')
    current_power=current_power.json()
    current_value=current_power['780']
    c = total_power.json()
    totalpower= c['801']['130']['100']
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
    trace0 = go.Bar(x=['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'], y=[mon, tue, wed, thu, fri, sat, sun],opacity=0.6,
             marker=dict(
        color='rgb(205, 12, 24)'
    ))
    trace1 = go.Scatter(y=y, x=x,
        line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4))
    data = [trace0]
    data2= [trace1]
    fig = go.Figure(data=data, layout=layout)
    my_plot_div = plot(fig, output_type='div')
    layout2 = go.Layout(title='Ayasli Ges Day Values', yaxis=dict(title='Wh(Wattshour)'))
    fig2 =  go.Figure(data=data2, layout= layout2)
    my_plot_div2 = plot(fig2, output_type='div')
    return render_template('index.html',div_placeholder= Markup(my_plot_div), div_placeholder2= Markup(my_plot_div2),value=current_value)

@app.route('/year', methods=['GET', 'POST'])
def year():
    #if request.method == 'POST'
    data = requests.post('http://144.122.167.229/getjp',data='token: ;{"877":null}')
    data=data.json()
    x = []
    y = []
    for i in range(0,11):
        x.append(data['877'][i][0])
        y.append(data['877'][i][1])
    trace0 = go.Bar(x=x, y=y,opacity=0.6,
    marker=dict(
    color='rgb(205, 12, 24)'
    ))
    layout = go.Layout(title='Ayasli Ges Yearly Power Output')
    data = [trace0]
    fig = go.Figure(data=data, layout=layout)
    my_plot_div3 = plot(fig, output_type='div')
    return render_template('year.html',div_placeholder3= Markup(my_plot_div3))
@app.route('/month', methods=['GET', 'POST'])
def month():
    month_data = requests.post('http://144.122.167.229/getjp', 'token: ;preval=none;{"141":{"32000":{"108":{"1":null},"118":null,"119":null,"145":null,"149":null,"158":null}},"152":null,"161":null,"162":null,"480":null,"777":{"3":null},"801":{"100":null}}')
    raw_data=month_data.json()
    data=raw_data['777']['3']
    x=[]
    y=[]
    sum = 0
    sumdata=[]
    for i in range(0,len(data)-1):
        y.append(data[i][0])
    for j in range(0,len(data)-1):
        for i in range(0,9):
            sum = sum + data[j][1][i]
        sumdata.append(sum)
    trace0=go.Bar(x=y, y=sumdata,opacity=0.6,
    marker=dict(
    color='rgb(205, 12, 24)'
    ))
    layout = go.Layout(title='Ayasli Ges Monthly Power Output')
    data = [trace0]
    fig = go.Figure(data=data, layout=layout)
    my_plot_div3 = plot(fig, output_type='div')
    return render_template('month.html',div_placeholder= Markup(my_plot_div3))

if __name__ == '__main__':
	app.run(port=5000, debug=True)
