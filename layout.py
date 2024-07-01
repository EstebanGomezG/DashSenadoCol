from dash import html, dcc

def create_layout(congresistas):
    return html.Div([
        dcc.Dropdown(
            id='congresista-dropdown',
            options=[
                {'label': row['nombre'], 'value': row['id']} for index, row in congresistas.iterrows()
            ],
            placeholder="Seleccione un congresista"
        ),
        html.Div(id='congresista-info', children=[
            html.Img(id='congresista-foto', height='150px', width='150px'),
            html.H4(id='congresista-nombre'),
            html.P(id='congresista-partido'),
            html.P(id='congresista-ultima-votacion'),
            html.P(id='congresista-bancada'),
            html.P(id='congresista-comision'),
            html.P(id='congresista-departamento'),
            html.P(id='congresista-perfil'),
            html.P(id='congresista-entidades'),
            html.P(id='congresista-debilidades'),
            html.P(id='congresista-apoyo-rechazo')
        ])
    ])

