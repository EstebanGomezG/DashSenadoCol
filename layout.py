from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px


def create_layout(congresistas):
    return html.Div([
        html.Br(),
        html.Br(),
        html.H1("Bienvenido a Senado_Col"),
        html.P(["Senado_Col es una herramienta de código abierto construida desde cero, para idear estrategias que contribuyan a optimizar la relación entre el Ejecutivo y el Senado en Colombia."
                "Esta plataforma usa metodologías mixtas de análisis político, con el propósito de contribuir a responder una pregunta clave:",
               html.Br(),
               html.Br(),
               html.H5("¿Cuáles podrían ser las estrategias más efectivas para que el Ejecutivo gane incidencia en el Senado, logrando así mayor eficacia legislativa en los meses de gobierno restantes?")]),
        dcc.Tabs([
            dcc.Tab(label='Distribución partidos', children=[
                html.P("El Gobierno de Gustavo Petro llegó al poder con un significativo respaldo popular en Colombia, consolidando una amplia base electoral que impulsó su campaña. Esto permitió que su Coalición Pacto Histórico fuera la coalición con el mayor número de curules tanto en La Cámara de Representantes como en el Senado de la República."),
                html.P("En el siguiente gráfico se puede observar la distribución de las curules del Senado de la República para el periodo 2022 – 2026:"),
                dcc.Graph(id="grafico-barras"),
                html.P("En el siguiente gráfico de hemiciclo se ilustra con mayor claridad la distribución de los escaños en el Senado de Colombia:"),
                dcc.Graph(id='grafico-hemiciclo'),
                html.P("Sin embargo, esto no se tradujo en lograr las mayorías legislativas en ninguna de las dos cámaras, siendo especialmente compleja la situación del Senado, donde ha encontrado importantes obstáculos."),
                html.P("Así las cosas, el ejecutivo ha enfrentado retos considerables para conseguir eficacia legislativa. La agenda de reformas, aunque ambiciosa y necesaria según muchos sectores, no ha logrado avanzar con la celeridad y contundencia esperadas. La complejidad del proceso legislativo, junto con diversas dinámicas internas del Senado, han limitado la capacidad del gobierno para implementar plenamente sus propuestas, evidenciando así las dificultades en transformar el mandato popular en resultados concretos dentro del ámbito parlamentario."),
                html.P(""),
            ]),
            dcc.Tab(label='Distribución Bancadas', children=[
                html.P("Como se puede observar, pese a que el partido de gobierno es el partido mayoritario, dado el comportamiento de los distintos congresistas, resulta evidente que éste se encuentra en abierta desventaja."),
                html.P("Así las cosas, el exito o fracaso en sus iniciativas legislativas depende de su capacidad para conformar lo que en Ciencia Política se conoce como Coalición Vencedora Mínima, y para ello debe que sumar votos de congresistas independientes y/o de oposición."),
                dcc.Graph(id='distribucion-bancadas'),
                html.P("Esta dependencia de respecto de los senadores de oposición e independientes se puede evidenciar si nos dentenemos a analizar los resultados de las votaciones del Senado en algunos de los proyectos de iniciativa gubernamental más importantes."),
            ]),
            dcc.Tab(label='Resultados de Votaciones', children=[
                html.P("Si bien el tramite legislativo en Colombia consta de varios debates y votaciones en Comisiones y Cámaras según el tipo de iniciativa, aquí nos restringimos a observar el comportamiento del Senado en Pleno en las votaciones definitorias, dado que es nuestro interés realizar el análisis exclusivo de esta cámara."),
                html.H1("NOTA: EL ANÁLISIS DETALLADO DE ESTOS RESULTADOS ESTÁ PENDIENTE"),
                dcc.Graph(id='barras-votaciones')
            ]),
            dcc.Tab(label='Perfiles Senadorxs', children=[
                html.Div([
                    html.P("A continuación se brindan elementos de análisis cualitativo que podrían facilitar la valoración de cada uno de los senadores de manera particular."),
                    html.P("NOTA: La información aquí suministrada no es más que la compilación de distintos rastreos de prensa y ejercicios de web scraping. De ahí que el creador de este sitio web no puede garantizar la completa vercidad y precisión de la misma. En consecuencia, tampoco se hace responsable de la contrastación de las noticias y registros de prensa sintetizados aquí."),
                    dcc.Dropdown(
                        id='congresista-dropdown',
                        options=[{'label': row['Nombre'], 'value': row['id']} for index, row in congresistas.iterrows()],
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

                            ], className='container')
                    ])
            ]),
            dcc.Tab(label='Insights', children=[
                html.H3("Conclusiones"),
                html.P("A partir del comportamiento electoral de los congresistas en los distintos proyectos de ley de iniciativa gubernamental analizados, se establece un puntaje de apoyo a las iniciativas de gobierno, para ponderar aquellos senadores de oposición o independientes que puedan resultar más proclives a apoyar futuras iniciativas de gobierno, siempre que se logre persuadirles en función de sus intereses políticos y burocraticos."),
                dcc.Graph(id='grafico-support'),
                html.P("Se concluye entonces que en situaciones donde el éxito legislativo de proyectos de iniciativa gubernamental, dependa de los votos de la oposición o de los independientes, será una buena estrategia del gobierno iniciar por intentar persuadir a los y las senadoras que tengan un mayor Support_Score."),
                html.P("Además del puntaje cuantitativo, disponer de los perfiles cualitativos de los congresistas puede contribuir a mejorar la estrategia. A futuro, quizá sea viable incluir en esta app un modelo de inteligencia artificial que sea capaz de incorporar en el análisis tanto los aspectos cuali como cuanti para mejorar el desempeño de esta herramienta que sigue en construcción.")
                            ])
        ]),
        html.H5("DISCLAIMER: "),
        html.P("Esta herramienta se ha creado exclusivamente con propósitos académicos y es de caracter puramente experimental. De ahí que el creador de la misma, pese a haber intentado un ejercicio juicioso de compilación de la información, no se hace responsable de la información aquí incluída. Así mismo, es menester advertir que los datos de congresistas, votaciones y curules por partido pueden ser imprecisos dado que se trata de datos dinamicos que podrían haber variado desde el momento en que se inició su recolección hasta el presente."),
        html.H5("Elaborado por: Esteban Gómez - Analista Político")

    ])
