import pandas as pd



def limpiar_datos(csv_file):
    df = pd.read_csv(csv_file)
    df = df.dropna()  # Eliminar filas con valores nulos
    df = df.reset_index(drop=True)
    print("DataFrame procesado:\n", df.head())
    return df

if __name__ == "__main__":
    limpiar_datos("data.csv")
