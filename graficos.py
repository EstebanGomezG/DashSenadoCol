import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import pandas as pd


def crear_grafico_hemiciclo(frecuencias_partido, colores_dict, num_filas=5):
    partidos = frecuencias_partido["Partido"]
    escanos = frecuencias_partido["Frecuencia"]
    total_escanos = sum(escanos)
    
    fig = go.Figure()
    start_angle = 0

    for idx, partido in enumerate(partidos):
        num_escanos = escanos.iloc[idx]
        color = colores_dict.get(partido, '#000000')  # Color del partido
        angle_span = (num_escanos / total_escanos) * 180

        # Listas para agrupar las coordenadas de los escaños por partido
        radios = []
        angulos = []
        
        for fila in range(num_filas):
            radio = 1.5 + fila * 0.3
            escanos_por_fila = int(np.ceil(num_escanos / num_filas))
            escaños_en_fila = min(escanos_por_fila, max(num_escanos - fila * escanos_por_fila, 0))
            if escaños_en_fila <= 0:
                continue
            
            fila_angles = np.linspace(start_angle, start_angle + angle_span, escaños_en_fila, endpoint=False)
            radios.extend([radio] * len(fila_angles))  # Mismos radios para cada fila
            angulos.extend(fila_angles)  # Ángulos calculados

        # Agregar una única traza para todos los escaños de este partido
        fig.add_trace(go.Scatterpolar(
            r=radios,
            theta=angulos,
            mode='markers',
            marker=dict(size=10, color=color),
            name=partido  # Una única entrada en la leyenda por partido
        ))

        start_angle += angle_span

    fig.update_layout(
        title='Curules por partido (Senado 2024)',
        polar=dict(
            radialaxis=dict(visible=False),
            angularaxis=dict(visible=False)
        ),
        showlegend=True  # Mostrar leyenda
    )
    return fig


def crear_grafico_barras(frecuencias_partido, colores_dict):
    # Ordenar los partidos por frecuencia descendente, si es necesario
    df_sorted = frecuencias_partido.sort_values(by='Frecuencia', ascending=False)
    
    # Crear el gráfico de barras
    fig_bar = px.bar(
        df_sorted,
        x='Partido',
        y='Frecuencia',
        color='Partido',
        color_discrete_map=colores_dict,
        title='Número de curules por partido'
    )
    
    # Personalizar el diseño
    fig_bar.update_layout(
        xaxis_title='Partido / Coalición',
        yaxis_title='Número de Curules',
        legend_title="Partidos",
        xaxis_tickangle=-45
    )
    
    return fig_bar

import pandas as pd
import plotly.express as px

def crear_grafico_barras_votaciones(congresistas):
    vot_cols = [
        "Vot_JuAgr_1", "Vot_JuAgr_2", "Vot_PazTotal",
        "Vot_Pensiones", "Vot_PND", "Vot_RefPol", "Vot_RefTrib"
    ]

    data = []
    for col in vot_cols:
        counts = congresistas[col].value_counts()
        for sentido, count in counts.items():
            data.append({"Proyecto": col, "Sentido": sentido, "Conteo": count})

    df_long = pd.DataFrame(data)

    # Diccionario de colores actualizado para los sentidos
    colores_votos = {
        'Sí': 'green',
        'No': 'red',
        'Ausente': 'gray'
    }

    fig = px.bar(
        df_long,
        x="Proyecto",
        y="Conteo",
        color="Sentido",
        color_discrete_map=colores_votos,  # Asignar colores personalizados
        barmode="group",
        title="Resultados de Votaciones por Proyecto"
    )

    fig.update_layout(
        xaxis_title="Proyecto de Ley",
        yaxis_title="Número de Votaciones",
        legend_title="Sentido de Voto"
    )

    return fig

def crear_grafico_mayor_support(congresistas, top_n=10):
    # Filtrar congresistas de oposición o independientes
    df_filtrado = congresistas[congresistas['Bancada'].isin(['Oposición', 'Independientes'])]
    
    # Ordenar descendientemente por Support_Score
    df_ordenado = df_filtrado.sort_values(by='Support_Score', ascending=False)
    
    # Seleccionar los top_n congresistas con mayor Support_Score
    top_df = df_ordenado.head(top_n)
    
    return top_df


def crear_grafico_barra_support(congresistas, top_n=10):
    # Obtener los datos preparados
    top_df = crear_grafico_mayor_support(congresistas, top_n)
    
    # Crear gráfico de barras horizontales
    fig = px.bar(
        top_df,
        y='Nombre',           
        x='Support_Score',
        orientation='h',       # Barra horizontal
        title=f"Top {top_n} Congresistas de Oposición e Independientes con mayor Puntaje de Apoyo a iniciativas de Gobierno"
    )
    
    # Ordenar los nombres en el eje y de mayor a menor Support_Score
    fig.update_yaxes(categoryorder='total ascending')
    
    return fig
