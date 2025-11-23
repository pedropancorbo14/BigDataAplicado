import pandas as pd
import os

# Cargar calificaciones
df = pd.read_csv("../../../Datasets/Datos_2022/Calificaciones.csv")

# Cargar cursos
df_cursos = pd.read_csv("../../../Datasets/Datos_2022/Cursos.csv")

# MERGE: unir por columna 'curso'
df = df.merge(df_cursos[["codigo", "nombre_cas"]], 
              left_on="curso", 
              right_on="codigo", 
              how="left")

# Agrupación
tabla_media = (
    df.groupby(["alumno", "curso", "nombre_cas", "anyo", "evaluacion"])["nota_numerica"]
      .mean()
      .reset_index()
)

tabla_media.rename(columns={"nota_numerica": "media_nota"}, inplace=True)

for _, row in tabla_media.iterrows():
    alumno = row["alumno"]
    curso = row["curso"]           
    nombre_cas = row["nombre_cas"]    
    anyo = row["anyo"]          
    evaluacion = row["evaluacion"]

    # Ruta final
    ruta = f"Analizados/{anyo}/Evaluaciones/{evaluacion}"
    os.makedirs(ruta, exist_ok=True)

    # Archivos de salida
    archivo_parquet = f"{ruta}/fact_media_calificaciones.parquet"
    archivo_csv = f"{ruta}/fact_media_calificaciones.csv"

    # Filtrar los datos correctos
    subset = tabla_media[
        (tabla_media["anyo"] == anyo) &
        (tabla_media["evaluacion"] == evaluacion)
    ]

    # Guardar parquet
    try:
        subset.to_parquet(archivo_parquet, index=False)
    except:
        print(f"❌ No se pudo guardar parquet en {archivo_parquet}. Falta pyarrow.")

    # Guardar CSV
    subset.to_csv(archivo_csv, index=False, sep=";")

print("Parquets y CSV creados por año y evaluación.")
