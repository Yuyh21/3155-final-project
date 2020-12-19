import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/usecon2010-2020.csv')
df['date'] = pd.to_datetime(df['date'])

df2 = pd.read_csv('../Datasets/stateunemployment2010-2020.csv')
df2['date'] = pd.to_datetime(df2['date'])

df3 = pd.read_csv('../Datasets/grossoutput1998-2019.csv')
df3['date'] = pd.to_datetime(df3['date'])

df4 = pd.read_csv('../Datasets/unemploymentAllStates.csv')

app = dash.Dash()

# Us econ Line Chart
data_salary = [go.Scatter(x=df['date'], y=df['avgsalary'], mode='lines', name='Average Salary',
                          line=dict(color='#09C100'))]
data_imports = [go.Scatter(x=df['date'], y=df['imports'], mode='lines', name='Import Index',
                           line=dict(color='#0058C1'))]
data_unemployment = [go.Scatter(x=df['date'], y=df['unemployment'], mode='lines', name='Unemployment',
                                line=dict(color='#B30000'))]

data_unemploymentbarchart = [go.Bar(x=df4['state'], y=df4['unemployment'])]

# Layout
app.layout = html.Div(children=[
    html.H1(children='US Economy',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('US economy statistics from 12/1/1998 to 10/1/2020', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Div('This app contains information pertaining to the US economy in various forms. Currently, there are '
             'unemployment rates, gross output for various industries, and how the US has done with importing goods '
             'over the last 10-20 years.',
             style={'textAlign': 'center', 'font-size': '30px'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'textAlign': 'center', 'color': '#7FDBFF'}),
    html.H3('Gross Output', style={'color': '#df1e56', 'font-size': '25px', 'textAlign': 'center'}),
    html.Div('This line chart represents the change in gross output per year by industry.',
             style={'textAlign': 'center'}),
    dcc.Graph(id='graph0'),
    html.Div('Please select an industry', style={'color': '#ef3e18', 'margin': '10px'}),
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
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Unemployment', style={'color': '#df1e56', 'font-size': '25px', 'textAlign': 'center'}),
    html.Div('This line chart represents the unemployment rate by individual state.',
             style={'textAlign': 'center'}),
    dcc.Graph(id='graph1'),
    html.Div('Please select a state', style={'color': '#ef3e18', 'margin': '10px'}),
    dcc.Dropdown(
        id='select-state',
        options=[
            {'label': 'North Carolina', 'value': 'nc'},
            {'label': 'Florida', 'value': 'fl'},
            {'label': 'New York', 'value': 'ny'},
        ],
        value='nc'
    ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Unemployment', style={'color': '#df1e56', 'font-size': '25px', 'textAlign': 'center'}),
    html.Div('This bar chart represents the unemployment rate as of the last update, Dec 19th, 2020.',
             style={'textAlign': 'center'}),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_unemploymentbarchart,
                  'layout': go.Layout(title='',
                                      xaxis={'title': 'State'}, yaxis={'title': 'Unemployment'},
                                      plot_bgcolor='#EBEBEB')
              }
              ),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Import Index', style={'color': '#df1e56', 'font-size': '25px', 'textAlign': 'center'}),
    html.Div('This line chart represents the import index in the United States from Jan 2010 through Oct 2020.',
             style={'textAlign': 'center'}),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_imports,
                  'layout': go.Layout(title='',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Index'},
                                      plot_bgcolor='#EBEBEB')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Unemployment', style={'color': '#df1e56', 'font-size': '25px', 'textAlign': 'center'}),
    html.Div('This line chart represents the unemployment rate in the united states from Jan 2010 through Oct 2020.',
             style={'textAlign': 'center'}),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_unemployment,
                  'layout': go.Layout(title='',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Unemployment'},
                                      plot_bgcolor='#EBEBEB')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Salary', style={'color': '#df1e56', 'font-size': '25px', 'textAlign': 'center'}),
    html.Div('This line chart represents the average salary of '
             'workers in the united states from Jan 2010 through Oct 2020.',
             style={'textAlign': 'center'}),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_salary,
                  'layout': go.Layout(title='',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Salary'},
                                      plot_bgcolor='#EBEBEB')

              }
              )
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


if __name__ == '__main__':
    app.run_server()
