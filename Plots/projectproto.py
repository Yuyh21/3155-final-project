import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/usecon2010-2020.csv')
df['date'] = pd.to_datetime(df['date'])

app = dash.Dash()

# Us econ Line Chart
data_salary = [go.Scatter(x=df['date'], y=df['avgsalary'], mode='lines', name='Average Salary')]
data_imports = [go.Scatter(x=df['date'], y=df['imports'], mode='lines', name='Import Index')]
data_unemployment = [go.Scatter(x=df['date'], y=df['unemployment'], mode='lines', name='Unemployment')]

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the average salary of '
             'workers in the united states from Jan 2010 through Oct 2020.'),
    dcc.Graph(id='graph1',
              figure={
                  'data': data_salary,
                  'layout': go.Layout(title='Avg Salary',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Salary'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the import index in the united states from Jan 2010 through Oct 2020.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_imports,
                  'layout': go.Layout(title='Import Index For the United States',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Index'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the unemployment rate in the united states from Jan 2010 through Oct 2020.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_unemployment,
                  'layout': go.Layout(title='Unemployment Rate in the United States',
                                      xaxis={'title': 'Date'}, yaxis={'title': 'Unemployment'})
              }
              )
])

if __name__ == '__main__':
    app.run_server()