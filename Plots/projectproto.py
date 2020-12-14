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

app = dash.Dash()

# Us econ Line Chart
data_salary = [go.Scatter(x=df['date'], y=df['avgsalary'], mode='lines', name='Average Salary')]
data_imports = [go.Scatter(x=df['date'], y=df['imports'], mode='lines', name='Import Index')]
data_unemployment = [go.Scatter(x=df['date'], y=df['unemployment'], mode='lines', name='Unemployment')]

# Layout
app.layout = html.Div(children=[
    html.H1(children='US Economy',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('US economy statistics from 1/1/2010 to 10/1/2020', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Interactive Line Chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the change in gross output per year by industry.'),
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
    html.H3('Interactive Line Chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the unemployment rate by state.'),
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
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the import index in the united states from Jan 2010 through Oct 2020.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_imports,
                  'layout': go.Layout(title='Import Index For the United States',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Index'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the unemployment rate in the united states from Jan 2010 through Oct 2020.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_unemployment,
                  'layout': go.Layout(title='Unemployment Rate in the United States',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Unemployment'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the average salary of '
             'workers in the united states from Jan 2010 through Oct 2020.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_salary,
                  'layout': go.Layout(title='Avg Salary',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Salary'})
              }
              )
])


@app.callback(Output('graph1', 'figure'),
              [Input('select-state', 'value')])
def update_figure(selected_state):
    new_df = df2[df2['state'] == selected_state]

    data_state_unemployment = [
        go.Scatter(x=new_df['date'], y=new_df['unemployment'], mode='lines', name='Unemployment')]
    return {'data': data_state_unemployment, 'layout': go.Layout(title='Unemployment rate in ' + selected_state,
                                                                 xaxis={'title': 'State'},
                                                                 yaxis={'title': 'Unemployment Rate'})}

@app.callback(Output('graph0', 'figure'),
              [Input('select-industry', 'value')])
def update_figure(selected_industry):
    new_df = df3[df3['industry'] == selected_industry]

    data_gross_output = [
        go.Scatter(x=new_df['date'], y=new_df['gross_output_change'], mode='lines', name='Unemployment')]
    return {'data': data_gross_output, 'layout': go.Layout(title='Gross Output Change in ' + selected_industry,
                                                                 xaxis={'title': 'Industry'},
                                                                 yaxis={'title': 'Gross Output'})}


if __name__ == '__main__':
    app.run_server()