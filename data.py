import pandas as pd

def load_data():
    df = pd.read_excel("Dash/senado_col/Senado_Col.xlsx", sheet_name="dis_senado")
    df['foto'] = df['id'].apply(lambda x: f'/assets/{x}.jpg')
    print(df.columns)
    return df