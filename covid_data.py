import plotly.graph_objects as go
import pandas as pd
import requests

n = 'Hungary'
m = 'Poland'

c1req = requests.get(
    f'https://disease.sh/v3/covid-19/historical/{n}?lastdays=all')
c1data = c1req.json()
c1dates = []
c1cases = []
c1recovered = []
c1deaths = []
for d in c1data['timeline']['cases']:
    c1dates.append(d)
    c1cases.append(c1data['timeline']['cases'][d])
for d in c1data['timeline']['recovered']:
    c1recovered.append(c1data['timeline']['recovered'][d])
for d in c1data['timeline']['deaths']:
    c1deaths.append(c1data['timeline']['deaths'][d])    

c2req = requests.get(
    f'https://disease.sh/v3/covid-19/historical/{m}?lastdays=all')
c2data = c2req.json()
c2dates = []
c2cases = []
c2recovered = []
c2deaths = []
for d in c2data['timeline']['cases']:
    c2dates.append(d)
    c2cases.append(c2data['timeline']['cases'][d])
for d in c2data['timeline']['recovered']:
    c2recovered.append(c2data['timeline']['recovered'][d])
for d in c2data['timeline']['deaths']:
    c2deaths.append(c2data['timeline']['deaths'][d])   

fig = go.Figure()
fig.add_trace(go.Scatter(x=c1dates, y=c1cases, name = f"Prípady - {n}"))
fig.add_trace(go.Scatter(x=c1dates, y=c1recovered, name = f"Vyliečení - {n}"))
fig.add_trace(go.Scatter(x=c1dates, y=c1deaths, name = f"Úmrtia - {n}"))
fig.add_trace(go.Scatter(x=c2dates, y=c2cases, name = f"Prípady - {m}"))
fig.add_trace(go.Scatter(x=c2dates, y=c2recovered, name = f"Vyliečení - {m}"))
fig.add_trace(go.Scatter(x=c2dates, y=c2deaths, name = f"Úmrtia - {m}"))

fig.show()
