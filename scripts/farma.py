import requests

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

    organizado_por_comuna = {}
    for farmacia in farmacias:
        comuna = farmacia['comuna_nombre']
        if comuna not in organizado_por_comuna:
            organizado_por_comuna[comuna] = []
        organizado_por_comuna[comuna].append(farmacia)
    
    for comuna, farmacias in organizado_por_comuna.items():
        print(f"Comuna: {comuna}")
        for farmacia in farmacias:
            print(f"  Nombre: {farmacia['local_nombre']}")
            print(f"  Dirección: {farmacia['local_direccion']}")
            print(f"  Teléfono: {farmacia['local_telefono']}")
            print(f"  Horario: {farmacia['funcionamiento_hora_apertura']} - {farmacia['funcionamiento_hora_cierre']}")
            print(f"  Latitud: {farmacia['local_lat']}, Longitud: {farmacia['local_lng']}")
            print("  ---")
        print("---------\n")

url = "https://midas.minsal.cl/farmacia_v2/WS/getLocales.php"
datos = obtener_datos(url)
organizar_datos(datos)
