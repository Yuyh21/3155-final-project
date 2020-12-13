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
    filtered_df = df2[df2['state'] == selected_state]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    new_df = filtered_df.groupby(['state']).sum().reset_index()
    data_interactive_barchart = [go.Bar(x=new_df['date'], y=new_df['unemployment'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Unemployment rate in '+selected_state,
                                                                   xaxis={'title': 'State'},
                                                                   yaxis={'title': 'Unemployment Rate'})}

if __name__ == '__main__':
    app.run_server()