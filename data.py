import pandas as pd
def load_data():
    df = pd.read_excel("C:\DATA\DashSenadoCol\Senado_Col.xlsx", sheet_name="Sheet1")
    df['foto'] = df['id'].apply(lambda x: f'/assets/{x}.jpg')
    return df