"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import re

def create_data(line):
    line_clear = re.sub(r"\s+", " ", line).strip()  # Elimina espacios extra
    x= line_clear.split("%")
    frist= x[0].split(" ")
    frist.pop()
    frist[len(frist)-1] = float(frist[len(frist)-1].replace(",", "."))
    second = x[1]
    second = second.replace(".","")
    second = second[1:]
    d = frist
    d.append(second)
    return d

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """


    import pandas as pd
    

    # Leer el archivo línea por línea
    with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Saltar encabezados innecesarios (las primeras 4 líneas)
    data_lines = lines[4:]

    # Procesar el archivo para consolidar filas que se desbordan
    data = []
    current_line = ""

    for line in data_lines:
        # Si la línea comienza con un número (nueva fila), guardar la anterior y empezar una nueva
        if re.match(r'^\s*\d+', line):
            if current_line:  # Guardar la fila anterior
                d = create_data(current_line)
                data.append(d)
            current_line = line.strip()  # Iniciar nueva fila
        else:
            # Continuar con la línea anterior
            current_line += " " + line.strip()

    # Agregar la última fila procesada
    if current_line:
        d = create_data(current_line)
        data.append(d)


    # Crear un DataFrame con columnas adecuadas
    columns = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]

    df = pd.DataFrame(data, columns=columns)

    df["cluster"] = df["cluster"].astype(int)
    df["cantidad_de_palabras_clave"] = df["cantidad_de_palabras_clave"].astype(int)
    df["principales_palabras_clave"] = df["principales_palabras_clave"].astype(str)


    return df


pregunta_01()