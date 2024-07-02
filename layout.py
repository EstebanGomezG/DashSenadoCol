from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px

def create_layout(congresistas):
    return html.Div([
        dcc.Tabs([
            dcc.Tab(label='Información del Congresista', children=[
                html.Div([
                    dcc.Dropdown(
                        id='congresista-dropdown',
                        options=[{'label': row['nombre'], 'value': row['id']} for index, row in congresistas.iterrows()],
                        placeholder='Seleccione un congresista'
                    ),
                    html.Div([
                        html.Img(id='congresista-foto', className='congresista-foto'),
                        html.H4(id='congresista-nombre', className='congresista-nombre'),
                        html.P([
                            html.Span('Partido: ', className='label'),
                            html.Span(id='congresista-partido')
                        ]),
                        html.P([
                            html.Span('Última votación: ', className='label'),
                            html.Span(id='congresista-ultima-votacion')
                        ]),
                        html.P([
                            html.Span('Bancada: ', className='label'),
                            html.Span(id='congresista-bancada')
                        ]),
                        html.P([
                            html.Span('Comisión: ', className='label'),
                            html.Span(id='congresista-comision')
                        ]),
                        html.P([
                            html.Span('Departamento: ', className='label'),
                            html.Span(id='congresista-departamento')
                        ]),
                        html.P([
                            html.Span('Perfil: ', className='label'),
                            html.Span(id='congresista-perfil')
                        ]),
                        html.P([
                            html.Span('Entidades: ', className='label'),
                            html.Span(id='congresista-entidades')
                        ]),
                        html.P([
                            html.Span('Debilidades: ', className='label'),
                            html.Span(id='congresista-debilidades')
                        ]),
                        html.P([
                            html.Span('Apoyo/Rechazo: ', className='label'),
                            html.Span(id='congresista-apoyo-rechazo')
                        ]),
                    ], className='congresista-info')
                ])
            ]),
            dcc.Tab(label='Distribución Bancadas', children=[
                dcc.Graph(id='distribucion-bancadas')
            ]),
            dcc.Tab(label='Distribución Partidos', children=[
                dcc.Graph(id='distribucion-partidos')
            ]),
            dcc.Tab(label='Resultados de Votaciones', children=[
                dcc.Dropdown(
                    id='proyecto-ley-dropdown',
                    options=[{'label': proyecto, 'value': proyecto} for proyecto in congresistas['proyecto_ley'].dropna().unique()],
                    placeholder='Seleccione un proyecto de ley'
                ),
                dcc.Graph(id='resultados-votaciones')
            ])
        ])
    ])
