import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

from app import app

# Load CSV file from Datasets folder
df = pd.read_csv('Datasets/usecon2010-2020.csv')
df['date'] = pd.to_datetime(df['date'])

df2 = pd.read_csv('Datasets/stateunemployment2010-2020.csv')
df2['date'] = pd.to_datetime(df2['date'])

df3 = pd.read_csv('Datasets/grossoutput1998-2019.csv')
df3['date'] = pd.to_datetime(df3['date'])

df4 = pd.read_csv('Datasets/unemploymentAllStates.csv')

# Us econ Line Chart
data_salary = [go.Scatter(x=df['date'], y=df['avgsalary'], mode='lines', name='Average Salary',
                          line=dict(color='#09C100'))]
data_imports = [go.Scatter(x=df['date'], y=df['imports'], mode='lines', name='Import Index',
                           line=dict(color='#0058C1'))]
data_unemployment = [go.Scatter(x=df['date'], y=df['unemployment'], mode='lines', name='Unemployment',
                                line=dict(color='#B30000'))]

data_unemploymentbarchart = [go.Bar(x=df4['state'], y=df4['unemployment'])]

layout = html.Div([
    dbc.Container([
        dbc.Row(dbc.Col(html.H3('Unemployment', style={'color': '#df1e56', 'font-size': '25px'}),
                        width={'size': 5, 'offset': 5}),
                ),
        dbc.Row(dbc.Col(html.Div('This line chart represents the unemployment rate by individual state.'),
                        ),
                ),
        dcc.Graph(id='graph1'),
        dbc.Row(dbc.Col(html.Div('Please select a state', style={'color': '#ef3e18', 'margin': '10px'}),
                        width={'size': 5, 'offset': 5}),
                ),
        dcc.Dropdown(
            id='select-state',
            options=[
                {'label': 'North Carolina', 'value': 'nc'},
                {'label': 'Florida', 'value': 'fl'},
                {'label': 'New York', 'value': 'ny'},
            ],
            value='nc'
        ),
        dbc.Row(html.Hr(style={'color': '#7FDBFF'}),
                ),
        dbc.Row(dbc.Col(html.H3('Unemployment', style={'color': '#df1e56', 'font-size': '25px'}),
                        width={'size': 5, 'offset': 5}),
                ),
        dbc.Row(
            dbc.Col(html.Div('This bar chart represents the unemployment rate as of the last update, Dec 19th, 2020.'),
                    ),
        ),
        dcc.Graph(id='graph2',
                  figure={
                      'data': data_unemploymentbarchart,
                      'layout': go.Layout(title='',
                                          xaxis={'title': 'State'}, yaxis={'title': 'Unemployment'},
                                          plot_bgcolor='#EBEBEB')
                  }
                  ),
        dbc.Row(html.Br()),
        dbc.Row(html.Br()),
        dbc.Row(html.Hr(style={'color': '#7FDBFF'}),
                ),
        dbc.Row(dbc.Col(html.H3('Unemployment', style={'color': '#df1e56', 'font-size': '25px'}),
                        width={'size': 5, 'offset': 5}),
                ),
        dbc.Row(
            dbc.Col(html.Div('This line chart represents the unemployment rate in the united states from Jan 2010 '
                             'through Oct 2020.'),
                    ),
        ),
        dcc.Graph(id='graph4',
                  figure={
                      'data': data_unemployment,
                      'layout': go.Layout(title='',
                                          xaxis={'title': 'Date'}, yaxis={'title': 'Unemployment'},
                                          plot_bgcolor='#EBEBEB')
                  }
                  ),
        dbc.Row(html.Br()),
        dbc.Row(html.Br())

    ])

])


@app.callback(Output('graph1', 'figure'),
              [Input('select-state', 'value')])
def update_figure(selected_state):
    new_df = df2[df2['state'] == selected_state]

    data_state_unemployment = [
        go.Scatter(x=new_df['date'], y=new_df['unemployment'], mode='lines', name='Unemployment',
                   line=dict(color='#7100F9'))]
    return {'data': data_state_unemployment, 'layout': go.Layout(title='',
                                                                 xaxis={'title': 'Date'},
                                                                 yaxis={'title': 'Unemployment Rate'},
                                                                 plot_bgcolor='#EBEBEB')}
