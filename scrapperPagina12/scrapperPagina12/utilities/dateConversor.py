# Diccionario para convertir los nombres de los meses
meses = {
    "enero": "01", "febrero": "02", "marzo": "03", "abril": "04", "mayo": "05", "junio": "06",
    "julio": "07", "agosto": "08", "septiembre": "09", "octubre": "10", "noviembre": "11", "diciembre": "12"
}


def convertirFecha2Iso(fecha):
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

        # Crear la fecha en formato ISO
        fecha_iso = f"{anio}-{mes_num}-{dia.zfill(2)}"

        return fecha_iso
    except Exception as e:
        # Devolver la fecha original con el mensaje de error
        return f"Error al convertir la fecha '{fecha_original}': {e}"