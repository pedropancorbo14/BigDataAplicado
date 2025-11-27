import pandas as pd
import sweetviz as sv
import numpy as np
import os

if not hasattr(np, 'VisibleDeprecationWarning'):
    np.VisibleDeprecationWarning = UserWarning
    
# Solicitar al usuario el nombre del archivo
file_path = input("Introduce el nombre del archivo con extensión (.csv, .xls o .xlsx): ")

# Extraer nombre sin extensión
nombre_sin_ext = os.path.splitext(file_path)[0]
nombre_html = nombre_sin_ext + ".html"

# Leer datos desde el archivo proporcionado por el usuario
if file_path.endswith('.csv'):
    separador = input("Introduce el separador del archivo CSV (por ejemplo, ',' o ';'): ")
    df = pd.read_csv(file_path, sep=separador, encoding='unicode_escape')
elif file_path.endswith('.xls') or file_path.endswith('.xlsx'):
    df = pd.read_excel(file_path)
else:
    raise ValueError("Formato de archivo no compatible. Utiliza archivos .csv, .xls o .xlsx.")

# Crear el perfil de análisis exploratorio de datos (EDA)
report = sv.analyze(df)

# Generar el informe HTML con el nombre del archivo de entrada
report.show_html(nombre_html)

print(f"Informe generado correctamente: {nombre_html}")
