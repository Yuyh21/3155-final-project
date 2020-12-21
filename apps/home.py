import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row(dbc.Col(html.H1('US Economic Timeline'), style={'color': '#00958A', 'textAlign': 'center'},
                        ),
                ),
        dbc.Row(html.Br()),
        dbc.Row(
            dbc.Col(html.Div('This app contains information pertaining to the US economy in various forms. Currently, '
                             'there are unemployment rates, gross output for various industries, and how the US has '
                             'done with importing goods over the last 10-20 years. Our plan is to add additional '
                             'information as it\'s needed, whether that be at the request of the people who use '
                             'this app, or if we come across something interesting enough that it has a good fit '
                             'here.'), style={'color': '#00958A', 'textAlign': 'center', 'font-size': '40px'},
                    ),
        ),
        dbc.Row(html.Br()),
        dbc.Row(html.Br()),
        dbc.Row(
            dbc.Col(html.Footer('If you have a piece of information or a set of statistics that you think is useful '
                                'please email placeholder@email.com and we will look into getting it added as long as '
                                'it\'s a good fit.'), style={'color': '#00958A', 'textAlign': 'center', 'font-size': '30px'},
                    ),
        ),
    ])

])
