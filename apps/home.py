import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
    dbc.Row(dbc.Col(html.H1("US Economy"), width={'size': 5, 'offset': 5},
                    ),
            ),
    dbc.Row(dbc.Col(html.Div('This app contains information pertaining to the US economy in various forms. Currently, '
                             'there are unemployment rates, gross output for various industries, and how the US has '
                             'done with importing goods over the last 10-20 years.'), width={'size': 6, 'offset': 3},
                    ),
            ),
    dbc.Row(html.Br())


    ])



])


