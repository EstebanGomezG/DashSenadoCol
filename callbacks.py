from dash.dependencies import Input, Output
import plotly.express as px
from graficos import crear_grafico_hemiciclo, crear_grafico_barras, crear_grafico_barras_votaciones, crear_grafico_barra_support

def register_callbacks(app, congresistas, frecuencias_partido, color_partido):
    @app.callback(
        [Output('congresista-foto', 'src'),
         Output('congresista-nombre', 'children'),
         Output('congresista-partido', 'children'),
         Output('congresista-ultima-votacion', 'children'),
         Output('congresista-bancada', 'children'),
         Output('congresista-comision', 'children'),
         Output('congresista-departamento', 'children'),
         Output('congresista-perfil', 'children'),
         Output('congresista-entidades', 'children'),
         Output('congresista-debilidades', 'children'),
         Output('congresista-apoyo-rechazo', 'children')],
        [Input('congresista-dropdown', 'value')]
    )
    def update_congresista_info(congresista_id):
        if congresista_id is None:
            return [None] * 11
        
        row = congresistas.loc[congresistas['id'] == congresista_id].iloc[0]
        
        return [
            row.get('foto', 'assets/default.png'),
            row.get('Nombre', 'Nombre no disponible'),
            row.get('Partido', 'Partido no disponible'),
            row.get('Ultima_Votacion', 'Última votación no disponible'),
            row.get('Bancada', 'Bancada no disponible'),
            row.get('Comision', 'Comisión no disponible'),
            row.get('Departamento', 'Departamento no disponible'),
            row.get('Perfil', 'Perfil no disponible'),
            row.get('Entidades', 'Entidades no disponibles'),
            row.get('Debilidades', 'Debilidades no disponibles'),
            row.get('Apoyo_Rechazo', 'Apoyo/Rechazo no disponible')
        ]

    @app.callback(
    Output('distribucion-bancadas', 'figure'),
    [Input('congresista-dropdown', 'value')]
    )
    def update_distribucion_bancadas(_):
        distribucion = congresistas['Bancada'].value_counts().reset_index()
        distribucion.columns = ['Bancada', 'count']
        
        colores = {
            'Oposición': '#4169E1',     # Azul rey
            'Gobierno': '#FF0000',      # Rojo
            'Independiente': '#808080' # Gris
        }
        
        
        fig = px.pie(
            distribucion,
            values='count',
            names='Bancada',
            title='Distribución Bancadas',
            color='Bancada',
            color_discrete_map=colores,
            width=800,   
            height=600
               
        )
        
        return fig
    
    @app.callback(
        Output('barras-votaciones', 'figure'),
        [Input('congresista-dropdown', 'value')]  
    )
    def update_barras_votaciones(_):
        fig = crear_grafico_barras_votaciones(congresistas)
        return fig

    @app.callback(
        Output('grafico-hemiciclo', 'figure'),
        [Input('congresista-dropdown', 'value')]  
    )
    def actualizar_hemiciclo(_):
        fig = crear_grafico_hemiciclo(frecuencias_partido, color_partido)
        return fig
    
    @app.callback(
    Output('grafico-barras', 'figure'),
    [Input('congresista-dropdown', 'value')]
    )
    def actualizar_barras(_):
        fig_bar = crear_grafico_barras(frecuencias_partido, color_partido)
        return fig_bar
    
    @app.callback(
    Output('grafico-support', 'figure'),
     [Input('congresista-dropdown', 'value')]
    )
    def actualizar_grafico_support(_):
        fig = crear_grafico_barra_support(congresistas, top_n=10)
        return fig