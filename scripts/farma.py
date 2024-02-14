import requests
import pandas as pd

def obtener_datos(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la respuesta no es exitosa
        return response.json()  # Retorna los datos como JSON
    except requests.RequestException as e:
        print(f"Error al obtener los datos: {e}")
        return None

def organizar_datos(farmacias):
    if farmacias is None:
        print("No hay datos para organizar.")
        return

    # Convertimos la lista de farmacias a un DataFrame de Pandas
    df = pd.DataFrame(farmacias)
    
    # Si necesitas reordenar o seleccionar columnas específicas, puedes hacerlo así:
    # df = df[['comuna_nombre', 'local_nombre', 'local_direccion', 'local_telefono', 'funcionamiento_hora_apertura', 'funcionamiento_hora_cierre', 'local_lat', 'local_lng']]
    
    return df

url = "https://midas.minsal.cl/farmacia_v2/WS/getLocales.php"
datos = obtener_datos(url)
df_farmacias = organizar_datos(datos)

if df_farmacias is not None:
    # Muestra las primeras filas del DataFrame para verificar los datos
    print(df_farmacias.head())
else:
    print("No se pudo crear el DataFrame.")
