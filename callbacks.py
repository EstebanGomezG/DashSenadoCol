from dash.dependencies import Input, Output
import plotly.express as px

def register_callbacks(app, congresistas):
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
            row.get('nombre', 'Nombre no disponible'),
            row.get('partido', 'Partido no disponible'),
            row.get('ultima_votacion', 'Última votación no disponible'),
            row.get('bancada', 'Bancada no disponible'),
            row.get('comision', 'Comisión no disponible'),
            row.get('departamento', 'Departamento no disponible'),
            row.get('perfil', 'Perfil no disponible'),
            row.get('entidades', 'Entidades no disponibles'),
            row.get('debilidades', 'Debilidades no disponibles'),
            row.get('apoyo_rechazo', 'Apoyo/Rechazo no disponible')
        ]

    @app.callback(
        Output('distribucion-bancadas', 'figure'),
        [Input('congresista-dropdown', 'value')]
    )
    def update_distribucion_bancadas(_):
        distribucion = congresistas['bancada'].value_counts().reset_index()
        distribucion.columns = ['bancada', 'count']
        fig = px.pie(distribucion, values='count', names='bancada', title='Distribución Bancadas')
        return fig
    
    @app.callback(
        Output('distribucion-partidos', 'figure'),
        [Input('congresista-dropdown', 'value')]
    )
    def update_distribucion_partidos(_):
        distribucion_part = congresistas['partido'].value_counts().reset_index()
        distribucion_part.columns = ['partido', 'count']
        fig = px.pie(distribucion_part, values='count', names='partido', title='Distribución Partidos')
        return fig

    @app.callback(
        Output('resultados-votaciones', 'figure'),
        [Input('proyecto-ley-dropdown', 'value')]
    )
    def update_resultados_votaciones(proyecto_ley):
        if proyecto_ley is None:
            return px.bar(title='Seleccione un proyecto de ley')

        votaciones = congresistas[congresistas['proyecto_ley'] == proyecto_ley]
        fig = px.bar(votaciones, x='nombre', y='voto', title=f'Resultados de Votación para {proyecto_ley}')
        return fig
