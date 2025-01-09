import os
import pandas as pd

def load_data():
    # Obtiene la ruta del directorio donde se encuentra este script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Construye la ruta relativa al archivo Excel dentro de la carpeta 'data'
    file_path = os.path.join(base_dir, 'data', 'Senado_Col.xlsx')
    
    # Lee el archivo Excel usando la ruta relativa construida
    df = pd.read_excel(file_path, sheet_name="Sheet1")
    df['foto'] = df['id'].apply(lambda x: f'/assets/{x}.jpg')
    return df
"""
def load_data():
    df = pd.read_excel("C:\DATA\DashSenadoCol\Senado_Col.xlsx", sheet_name="Sheet1")
    df['foto'] = df['id'].apply(lambda x: f'/assets/{x}.jpg')
    return df
"""