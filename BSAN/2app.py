
import dash
from dash import Dash
import dash_bootstrap_components as dbc


app = Dash(
	__name__, external_stylesheets=[dbc.themes.SLATE],
	use_pages=True
)

app.layout = dbc.Container(
	children=[
		dbc.NavbarSimple(
			brand="NHL",
			children=[
				dbc.NavItem( dbc.NavLink('Line Plot', href='/') ),
				dbc.NavItem( dbc.NavLink('Second Page', href='/page2') ),
			],
			color='primary',
			dark=True,
		),
		dash.page_container,
	],
	fluid=True,
)

if __name__ == '__main__':
	app.run_server(debug=True)