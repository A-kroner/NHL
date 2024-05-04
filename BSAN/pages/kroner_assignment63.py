import dash
from dash import dcc, html , Input , Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page( __name__, path='/' )
server=app.server
data = """
Player,Stats,Year,Value
Wayne Gretzky,Goals,1,51
Wayne Gretzky,Goals,2,55
Wayne Gretzky,Goals,3,92
Wayne Gretzky,Goals,4,71
Wayne Gretzky,Goals,5,87
Wayne Gretzky,Goals,6,73
Wayne Gretzky,Goals,7,52
Wayne Gretzky,Goals,8,62
Wayne Gretzky,Goals,9,40
Wayne Gretzky,Goals,10,54
Wayne Gretzky,Goals,11,40
Wayne Gretzky,Goals,12,41
Wayne Gretzky,Goals,13,31
Wayne Gretzky,Goals,14,16
Wayne Gretzky,Goals,15,38
Wayne Gretzky,Goals,16,11
Wayne Gretzky,Goals,17,15
Wayne Gretzky,Goals,18,8
Wayne Gretzky,Goals,19,25
Wayne Gretzky,Goals,20,23
Wayne Gretzky,Goals,22,9
Wayne Gretzky,Goals,23,.
Wayne Gretzky,Assists,1,86
Wayne Gretzky,Assists,2,109
Wayne Gretzky,Assists,3,120
Wayne Gretzky,Assists,4,125
Wayne Gretzky,Assists,5,118
Wayne Gretzky,Assists,6,135
Wayne Gretzky,Assists,7,163
Wayne Gretzky,Assists,8,121
Wayne Gretzky,Assists,9,109
Wayne Gretzky,Assists,10,114
Wayne Gretzky,Assists,11,102
Wayne Gretzky,Assists,12,122
Wayne Gretzky,Assists,13,90
Wayne Gretzky,Assists,14,49
Wayne Gretzky,Assists,15,92
Wayne Gretzky,Assists,16,37
Wayne Gretzky,Assists,17,66
Wayne Gretzky,Assists,18,13
Wayne Gretzky,Assists,19,72
Wayne Gretzky,Assists,20,67
Wayne Gretzky,Assists,22,53
Wayne Gretzky,Assists,23,.
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
Wayne Gretzky,Points,22,62
Wayne Gretzky,Points,23,.
Alex Ovechkin,Goals,1,52
Alex Ovechkin,Goals,2,46
Alex Ovechkin,Goals,3,65
Alex Ovechkin,Goals,4,56
Alex Ovechkin,Goals,5,50
Alex Ovechkin,Goals,6,32
Alex Ovechkin,Goals,7,38
Alex Ovechkin,Goals,8,32
Alex Ovechkin,Goals,9,51
Alex Ovechkin,Goals,10,53
Alex Ovechkin,Goals,11,50
Alex Ovechkin,Goals,12,33
Alex Ovechkin,Goals,13,49
Alex Ovechkin,Goals,14,51
Alex Ovechkin,Goals,15,48
Alex Ovechkin,Goals,16,24
Alex Ovechkin,Goals,17,50
Alex Ovechkin,Goals,18,42
Alex Ovechkin,Goals,19,16
Alex Ovechkin,Goals,20,.
Alex Ovechkin,Goals,22,.
Alex Ovechkin,Goals,23,.
Alex Ovechkin,Assists,1,54
Alex Ovechkin,Assists,2,46
Alex Ovechkin,Assists,3,47
Alex Ovechkin,Assists,4,54
Alex Ovechkin,Assists,5,59
Alex Ovechkin,Assists,6,53
Alex Ovechkin,Assists,7,27
Alex Ovechkin,Assists,8,24
Alex Ovechkin,Assists,9,28
Alex Ovechkin,Assists,10,28
Alex Ovechkin,Assists,11,21
Alex Ovechkin,Assists,12,36
Alex Ovechkin,Assists,13,38
Alex Ovechkin,Assists,14,38
Alex Ovechkin,Assists,15,19
Alex Ovechkin,Assists,16,18
Alex Ovechkin,Assists,17,40
Alex Ovechkin,Assists,18,33
Alex Ovechkin,Assists,19,27
Alex Ovechkin,Assists,20,.
Alex Ovechkin,Assists,22,.
Alex Ovechkin,Assists,23,.
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
Jaromir Jagr,Goals,1,62
Jaromir Jagr,Goals,2,47
Jaromir Jagr,Goals,3,35
Jaromir Jagr,Goals,4,44
Jaromir Jagr,Goals,5,42
Jaromir Jagr,Goals,6,52
Jaromir Jagr,Goals,7,31
Jaromir Jagr,Goals,8,36
Jaromir Jagr,Goals,9,16
Jaromir Jagr,Goals,10,15
Jaromir Jagr,Goals,11,54
Jaromir Jagr,Goals,12,30
Jaromir Jagr,Goals,13,25
Jaromir Jagr,Goals,14,19
Jaromir Jagr,Goals,15,14
Jaromir Jagr,Goals,16,2
Jaromir Jagr,Goals,17,24
Jaromir Jagr,Goals,18,11
Jaromir Jagr,Goals,19,6
Jaromir Jagr,Goals,20,27
Jaromir Jagr,Goals,22,16
Jaromir Jagr,Goals,23,1
Jaromir Jagr,Assists,1,87
Jaromir Jagr,Assists,2,48
Jaromir Jagr,Assists,3,67
Jaromir Jagr,Assists,4,83
Jaromir Jagr,Assists,5,54
Jaromir Jagr,Assists,6,69
Jaromir Jagr,Assists,7,48
Jaromir Jagr,Assists,8,41
Jaromir Jagr,Assists,9,29
Jaromir Jagr,Assists,10,14
Jaromir Jagr,Assists,11,69
Jaromir Jagr,Assists,12,66
Jaromir Jagr,Assists,13,46
Jaromir Jagr,Assists,14,35
Jaromir Jagr,Assists,15,12
Jaromir Jagr,Assists,16,7
Jaromir Jagr,Assists,17,43
Jaromir Jagr,Assists,18,18
Jaromir Jagr,Assists,19,12
Jaromir Jagr,Assists,20,39
Jaromir Jagr,Assists,22,30
Jaromir Jagr,Assists,23,6
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
Jaromir Jagr,Points,22,46
Jaromir Jagr,Points,23,7
"""


df = pd.read_excel('NHL_Player.xlsx')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

app.layout = html.Div([
    html.H1("NHL Player Stats"),
    html.P(
            'Let\'s compare the current scoring leader in the NHL in total career goals and assists to the player who holds the most total goals in a career playing in the NHL. Alex Ovechkin is still playing and is getting closer to Wayne Gretzky who holds the most goals, assists, and total points. We also add Jarmior Jagar who has the second most points in the NHL for comparison.',
            style=dict(textAlign='center')
        ),
    ]
)

html.Div([
        dcc.Dropdown(
            id='player-dropdown',
            options=[{'label': player, 'value': player} for player in df['Player'].unique()],
            value='Wayne Gretzky'
        ),
        dcc.RadioItems(
            id='stats-radio',
            options=[{'label': stat, 'value': stat} for stat in df['Stats'].unique() if stat != 'Points'],
            value='Goals',
            labelStyle={'display': 'inline-block'}
        )
    
  ]) 
    
dcc.Graph(id='line-plot')
 
   
    

@app.callback(
    Output('line-plot', 'figure'),
    [Input('player-dropdown', 'value'),
     Input('stats-radio', 'value')]
)
def update_line_plot(selected_player, selected_stat):
    filtered_df = df[(df['Player'] == selected_player) & (df['Stats'] == selected_stat)]
    fig = px.line(filtered_df, x='Year', y='Value', title=f'{selected_stat} of {selected_player}')
    return fig





# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
