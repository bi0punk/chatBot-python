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
    
    # Convertimos la lista de farmacias a un DataFrame
    df_farmacias = pd.DataFrame(farmacias)
    
    # Renombramos las columnas según los requerimientos
    df_farmacias_renombrado = df_farmacias.rename(columns={
        'comuna_nombre': 'Comuna',
        'local_nombre': 'Nombre',
        'local_direccion': 'Dirección',
        'local_telefono': 'Teléfono',
        'funcionamiento_hora_apertura': 'Hora Apertura',
        'funcionamiento_hora_cierre': 'Hora Cierre',
        'local_lat': 'Latitud',
        'local_lng': 'Longitud'
    })
    
    # Creamos la columna 'Horario' combinando 'Hora Apertura' y 'Hora Cierre'
    df_farmacias_renombrado['Horario'] = df_farmacias_renombrado['Hora Apertura'] + ' - ' + df_farmacias_renombrado['Hora Cierre']
    
    # Eliminamos las columnas de 'Hora Apertura' y 'Hora Cierre'
    df_farmacias_renombrado.drop(['Hora Apertura', 'Hora Cierre'], axis=1, inplace=True)
    
    # Seleccionamos el orden de las columnas
    df_farmacias_final = df_farmacias_renombrado[['Comuna', 'Nombre', 'Dirección', 'Teléfono', 'Horario', 'Latitud', 'Longitud']]
    
    # Ordenamos las comunas de manera alfabética
    df_farmacias_final = df_farmacias_final.sort_values(by='Comuna')
    
    return df_farmacias_final

url = "https://midas.minsal.cl/farmacia_v2/WS/getLocales.php"
datos = obtener_datos(url)
df_farmacias = organizar_datos(datos)

if df_farmacias is not None:
    # Muestra las primeras filas del DataFrame para verificar los datos
    print(df_farmacias.head(50))
else:
    print("No se pudo crear el DataFrame.")
