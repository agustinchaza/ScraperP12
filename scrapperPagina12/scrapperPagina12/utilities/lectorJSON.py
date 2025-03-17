import json


def cargar_configuracion():
    with open('config.json', 'r') as file:
        return json.load(file)
