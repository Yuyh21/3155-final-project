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
        dbc.Row(html.Hr(style={'color': '#7FDBFF'}),
                ),
        dbc.Row(dbc.Col(html.H3('Gross Output', style={'color': '#df1e56', 'font-size': '25px'}),
                        width={'size': 5, 'offset': 5}),
                ),
        dbc.Row(
            dbc.Col(html.Div('This line chart represents the change in gross output per year by industry.'),
                    ),
            ),
        dcc.Graph(id='graph0'),
        dbc.Row(dbc.Col(html.Div('Please select an industry', style={'color': '#ef3e18', 'margin': '10px'}),
                        ),
                ),
    dcc.Dropdown(
        id='select-industry',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'Farms', 'value': 'farms'},
            {'label': 'Oil and Gas', 'value': 'oil_and_gas'},
            {'label': 'Utilities', 'value': 'utilities'},
            {'label': 'Construction', 'value': 'construction'},
            {'label': 'Manufacturing', 'value': 'manufacturing'},
            {'label': 'Wholesale Trade', 'value': 'wholesale_trade'},
            {'label': 'Retail Trade', 'value': 'retail_trade'},
            {'label': 'Air Transportation', 'value': 'air_transportation'},
            {'label': 'Real Estate', 'value': 'real_estate'},
        ],
        value='all'
        ),
        dbc.Row(html.Br()),
        dbc.Row(html.Hr(style={'color': '#7FDBFF'}),
                ),
        dbc.Row(dbc.Col(html.H3('Import Index', style={'color': '#df1e56', 'font-size': '25px'}),
                        width={'size': 5, 'offset': 5}),
                ),
        dbc.Row(
            dbc.Col(html.Div('This line chart represents the import index in the United States from Jan 2010 through Oct 2020.'),
                    ),
            ),
        dcc.Graph(id='graph3',
                  figure={
                      'data': data_imports,
                      'layout': go.Layout(title='',
                                          xaxis={'title': 'Date'}, yaxis={'title': 'Index'},
                                          plot_bgcolor='#EBEBEB')
                  }
                  ),
        dbc.Row(html.Br()),
        dbc.Row(html.Hr(style={'color': '#7FDBFF'}),
                ),
        dbc.Row(dbc.Col(html.H3('Salary', style={'color': '#df1e56', 'font-size': '25px'}),
                        width={'size': 5, 'offset': 5}),
                ),
        dbc.Row(
            dbc.Col(html.Div('This line chart represents the average salary of '
             'workers in the united states from Jan 2010 through Oct 2020.'),
                    ),
            ),
        dcc.Graph(id='graph5',
                  figure={
                      'data': data_salary,
                      'layout': go.Layout(title='',
                                          xaxis={'title': 'Date'}, yaxis={'title': 'Salary'},
                                          plot_bgcolor='#EBEBEB')

                  }
                  )

        ])

    ])

@app.callback(Output('graph0', 'figure'),
              [Input('select-industry', 'value')])
def update_figure(selected_industry):
    new_df = df3[df3['industry'] == selected_industry]

    data_gross_output = [
        go.Scatter(x=new_df['date'], y=new_df['gross_output_change'], mode='lines', name='Unemployment')]
    return {'data': data_gross_output, 'layout': go.Layout(title='',
                                                           xaxis={'title': 'Date'},
                                                           yaxis={'title': 'Gross Output'},
                                                           plot_bgcolor='#EBEBEB')}

