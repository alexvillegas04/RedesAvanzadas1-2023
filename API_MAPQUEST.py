import time
import os
import requests
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "59dFcxrL3KjHOxYVWgdYJxRJ4Zd6ZjxH"


def mostrar_cargando():
    print("Cargando", end="")
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()
    print(
          " _______ _______ ______ _______ _______ _______ _______ _______\n"
          "|   |   |   _   |   __ \       |   |   |    ___|     __|_     _|\n"
          "|       |       |    __/   -  _|   |   |    ___|__     | |   |  \n"
          "|__|_|__|___|___|___|  |_______|_______|_______|_______| |___|\n")
    print("                                               ALEX Y ROBERTO")
    time.sleep(2)

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    print('Si desea salir introduzca: "salir o S"')

    orig = input("\nIngrese su origen (Ciudad, País): ")
    if orig == "salir" or orig == "S":
        break

    dest = input("Ingrese su destino (Ciudad, País): ")
    if dest == "salir" or dest == "S":
        break

    limpiar_consola()
    mostrar_cargando()

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest, "unit": "k"})

    data = requests.get(url).json()
    status = data["info"]["statuscode"]

    if status == 0:
        limpiar_consola()
        print("Datos ingresados: Correctos")
        print("================================================================")
        print("Informacion del viaje desde " + orig + " hasta " + dest)
        print("Duracion del viaje: " + data["route"]["formattedTime"]+" hrs/min/seg")
        print("Distancia: " + str(data["route"]["distance"]) + " km")
        print("================================================================")
        print("                                  ______")
        print("                                 /|_||_\\`.__")
        print("                                (   _    _ _\\")
        print("_________________________________`-(_)--(_)-____________________")
        print("\n")
