from dash.dependencies import Input, Output

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
            row['foto'],
            row['nombre'],
            row['partido'],
            row['ultima_votacion'],
            row['bancada'],
            row['comision'],
            row['departamento'],
            row['perfil'],
            row['entidades'],
            row['debilidades'],
            row['apoyo_rechazo']
        ]
