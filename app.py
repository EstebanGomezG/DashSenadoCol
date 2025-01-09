import dash
import dash_bootstrap_components as dbc
from data import load_data
from layout import create_layout
from callbacks import register_callbacks

congresistas = load_data()

frecuencias_partido = congresistas['Partido'].value_counts().reset_index()
frecuencias_partido.columns = ['Partido', 'Frecuencia']
color_partido = {
        "Pacto Histórico" : "#C63CD6",
        "Partido Conservador" : "#001170",
        "Coalición Centro Esperanza" : "#509922",
        "Partido Liberal" : "#DB0F00",
        "Centro Democrático" : "#5080B2",
        "Cambio Radical" : "#FA1B68",
        "De La U" : "#F57E00",
        "Comunes" : "#F43A36",
        "Alianza Cristiana" : "#1A82F5",
        "Curules Indígenas" : "#B9E59E"
    }


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = create_layout(congresistas)

register_callbacks(app, congresistas, frecuencias_partido, color_partido)


if __name__ == '__main__':
    app.run_server(debug=True)



