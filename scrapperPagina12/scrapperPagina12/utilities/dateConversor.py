from datetime import datetime

# Diccionario para convertir los nombres de los meses
meses = {
    "enero": "01", "febrero": "02", "marzo": "03", "abril": "04", "mayo": "05", "junio": "06",
    "julio": "07", "agosto": "08", "septiembre": "09", "octubre": "10", "noviembre": "11", "diciembre": "12"
}

def convertirFecha2Datetime(fecha):
    try:
        # Limpiar la fecha de caracteres extraños y convertir todo a minúsculas
        fecha_original = fecha  # Guardar la fecha original
        fecha = fecha.lower().strip()
        fecha = fecha.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

        # Separar la fecha en componentes
        partes = fecha.split(" de ")
        if len(partes) != 3:
            raise ValueError("La fecha no tiene el formato esperado.")

        dia = partes[0]
        mes = partes[1]
        anio = partes[2]

        # Convertir mes de texto a número
        mes_num = meses.get(mes)
        if not mes_num:
            raise ValueError(f"Mes no válido: {mes}")

        # Convertir a objeto datetime.date
        fecha_datetime = datetime.strptime(f"{anio}-{mes_num}-{dia.zfill(2)}", "%Y-%m-%d").date()

        return fecha_datetime
    except Exception as e:
        # Devolver None y el mensaje de error
        print(f"Error al convertir la fecha '{fecha_original}': {e}")
        return None

"""# Ejemplo de uso
fecha = "3 de marzo de 2024"
print(convertirFecha2Datetime(fecha))  # Salida: 2024-03-03
fechaLimite= "01-01-2000"
fechaLimite = datetime.strptime(fechaLimite, "%d-%m-%Y").date()
print(fechaLimite)  # Salida: 2000-01-01
#tipo de dato:
"""