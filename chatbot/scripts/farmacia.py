import requests

URL_FARMACIAS = "https://midas.minsal.cl/farmacia_v2/WS/getLocales.php"


def obtener_datos(url=URL_FARMACIAS):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error al obtener los datos: {e}")
        return None


def organizar_por_comuna(farmacias):
    if farmacias is None:
        print("No hay datos para organizar.")
        return {}
    resultado = {}
    for farmacia in farmacias:
        comuna = farmacia["comuna_nombre"]
        if comuna not in resultado:
            resultado[comuna] = []
        resultado[comuna].append(farmacia)
    return resultado


def imprimir_por_comuna(organizado):
    for comuna, farmacias in organizado.items():
        print(f"Comuna: {comuna}")
        for farmacia in farmacias:
            print(
                "  {local_nombre} ({local_direccion}) - {local_telefono}".format(
                    local_nombre=farmacia.get("local_nombre", "N/A"),
                    local_direccion=farmacia.get("local_direccion", "N/A"),
                    local_telefono=farmacia.get("local_telefono", "N/A"),
                )
            )
        print()


def a_dataframe(farmacias):
    import pandas as pd
    df = pd.DataFrame(farmacias)
    df = df.rename(
        columns={
            "comuna_nombre": "Comuna",
            "local_nombre": "Nombre",
            "local_direccion": "Direccion",
            "local_telefono": "Telefono",
            "funcionamiento_hora_apertura": "Hora Apertura",
            "funcionamiento_hora_cierre": "Hora Cierre",
        }
    )
    df["Horario"] = df["Hora Apertura"].astype(str) + " - " + df["Hora Cierre"].astype(str)
    df = df.drop(["Hora Apertura", "Hora Cierre"], axis=1)
    df = df.sort_values(by="Comuna")
    return df[["Comuna", "Nombre", "Direccion", "Telefono", "Horario"]]


if __name__ == "__main__":
    datos = obtener_datos()
    if datos:
        organizado = organizar_por_comuna(datos)
        imprimir_por_comuna(organizado)
    else:
        print("No se pudieron obtener los datos de farmacias.")
