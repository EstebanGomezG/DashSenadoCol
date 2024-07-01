from dash import dcc, html
import dash_bootstrap_components as dbc

def create_layout(congresistas):
    options = [{'label': row['nombre'], 'value': row['id']} for index, row in congresistas.iterrows()]
    
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("Perfiles Senadores"),
                dcc.Dropdown(
                    id='congresista-dropdown',
                    options=options,  # Aquí se pasa la lista de opciones generada
                    placeholder="Seleccione un congresista",
                )
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Img(id='congresista-foto', src='', height='200px', width='200px'),
                        html.H4(id='congresista-nombre', className='card-title'),
                        html.H6(id='congresista-partido'),
                        html.H6(id='congresista-ultima-votacion'),
                        html.H6(id='congresista-bancada'),
                        html.H6(id='congresista-comision'),
                        html.H6(id='congresista-departamento'),
                        html.P(id='congresista-perfil'),
                        html.P(id='congresista-entidades'),
                        html.P(id='congresista-debilidades'),
                        html.P(id='congresista-apoyo-rechazo')
                    ])
                ])
            ])
        ])
    ])

