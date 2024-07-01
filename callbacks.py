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
        print(f"congresista_id: {congresista_id}")  # Imprimir el ID del congresista seleccionado
        if congresista_id is None:
            return ['', '', '', '', '', '', '', '', '', '', '']

        row = congresistas.loc[congresistas['id'] == congresista_id]
        print(f"row: {row}")  # Imprimir la fila correspondiente

        if row.empty:
            return ['', '', '', '', '', '', '', '', '', '', '']

        row = row.iloc[0]
        
        return (
            row["foto"],
            row['nombre'],
            f"Partido: {row['partido']}",
            f"Última votación: {row['ultima_votacion']}",
            f"Bancada: {row['bancada']}",
            f"Comisión: {row['comision']}",
            f"Departamento: {row['departamento']}",
            f"Perfil: {row['perfil_politico']}",
            f"Entidades de incidencia: {row['entidades_incidencia']}",
            f"Debilidades: {row['debilidades']}",
            f"Apoyo/Rechazo a proyectos: {row['apoyo_rechazo']}"
        )
