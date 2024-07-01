import dash
import dash_bootstrap_components as dbc
from data import load_data
from layout import create_layout
from callbacks import register_callbacks

congresistas = load_data()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = create_layout(congresistas)

register_callbacks(app, congresistas)


if __name__ == '__main__':
    app.run_server(debug=True)



