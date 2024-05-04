
import dash
from dash import dcc, html , Input , Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


data = """
Player,Stats,Year,Value
Wayne Gretzky,Points,1,137
Wayne Gretzky,Points,2,164
Wayne Gretzky,Points,3,212
Wayne Gretzky,Points,4,196
Wayne Gretzky,Points,5,205
Wayne Gretzky,Points,6,208
Wayne Gretzky,Points,7,215
Wayne Gretzky,Points,8,183
Wayne Gretzky,Points,9,149
Wayne Gretzky,Points,10,168
Wayne Gretzky,Points,11,142
Wayne Gretzky,Points,12,163
Wayne Gretzky,Points,13,121
Wayne Gretzky,Points,14,65
Wayne Gretzky,Points,15,130
Wayne Gretzky,Points,16,48
Wayne Gretzky,Points,17,81
Wayne Gretzky,Points,18,21
Wayne Gretzky,Points,19,97
Wayne Gretzky,Points,20,90
Wayne Gretzky,Points,21,62
Wayne Gretzky,Points,22,.
Alex Ovechkin,Points,1,106
Alex Ovechkin,Points,2,92
Alex Ovechkin,Points,3,112
Alex Ovechkin,Points,4,110
Alex Ovechkin,Points,5,109
Alex Ovechkin,Points,6,85
Alex Ovechkin,Points,7,65
Alex Ovechkin,Points,8,56
Alex Ovechkin,Points,9,79
Alex Ovechkin,Points,10,81
Alex Ovechkin,Points,11,71
Alex Ovechkin,Points,12,69
Alex Ovechkin,Points,13,87
Alex Ovechkin,Points,14,89
Alex Ovechkin,Points,15,67
Alex Ovechkin,Points,16,42
Alex Ovechkin,Points,17,90
Alex Ovechkin,Points,18,75
Alex Ovechkin,Points,19,43
Alex Ovechkin,Points,20,.
Alex Ovechkin,Points,22,.
Alex Ovechkin,Points,23,.
Jaromir Jagr,Points,1,149
Jaromir Jagr,Points,2,95
Jaromir Jagr,Points,3,102
Jaromir Jagr,Points,4,127
Jaromir Jagr,Points,5,96
Jaromir Jagr,Points,6,121
Jaromir Jagr,Points,7,79
Jaromir Jagr,Points,8,77
Jaromir Jagr,Points,9,45
Jaromir Jagr,Points,10,29
Jaromir Jagr,Points,11,123
Jaromir Jagr,Points,12,96
Jaromir Jagr,Points,13,71
Jaromir Jagr,Points,14,54
Jaromir Jagr,Points,15,26
Jaromir Jagr,Points,16,9
Jaromir Jagr,Points,17,67
Jaromir Jagr,Points,18,29
Jaromir Jagr,Points,19,18
Jaromir Jagr,Points,20,66
Jaromir Jagr,Points,21,46
Jaromir Jagr,Points,22,7
"""


df = pd.read_excel('NHLPoints.xlsx')

df_points = df[df['Stats'] == 'points']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE] )
server=app.server

app.layout = html.Div([
    html.H1("NHL Player Points"),
    html.P(
            'Let\'s compare the current scoring leader in the NHL in total career points to a couple other players',
            style=dict(textAlign='center')
        ),
        dcc.Dropdown(
            id='player-dropdown',
            options=[{'label': player, 'value': player} for player in df['Player'].unique()],
            value='Wayne Gretzky'
        ),
    
    dcc.Graph(id='line-points' , figure={})
])


@app.callback(
    Output('line-points', 'figure'),
    Input('player-dropdown', 'value')
    )

def update_graph(selected_value ,):
    fdf = df[(df['Player'] == selected_value) ]

    line = px.line(fdf, x='Year' , y='Value', title=f'{selected_value.capitalize()} over Years')
    return line

if __name__ == '__main__':
    app.run_server(debug=True)
