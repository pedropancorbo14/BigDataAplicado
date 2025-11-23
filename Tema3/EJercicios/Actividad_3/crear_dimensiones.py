import pandas as pd
import os

base_path = "../../../Datasets/Datos_2022/"

# Crear carpeta de dimensiones
os.makedirs("Dimensiones", exist_ok=True)

# ------------------------------
# 1. DIMENSION ALUMNO
# ------------------------------

df_alumnos = pd.read_csv(base_path + "Alumnos.csv")

# Quitar duplicados
df_alumnos = df_alumnos.drop_duplicates(subset=["NIA"])

df_alumnos.to_csv("Dimensiones/dim_alumno.csv", index=False, sep=";")

# ------------------------------
# 2. DIMENSION CURSO
# ------------------------------

df_cursos = pd.read_csv(base_path + "Cursos.csv")

df_cursos = df_cursos.drop_duplicates(subset=["codigo"])

df_cursos.rename(columns={"codigo": "curso_id"}, inplace=True)

df_cursos.to_csv("Dimensiones/dim_curso.csv", index=False, sep=";")

# ------------------------------
# 3. DIMENSION MODULO
# ------------------------------

df_modulos = pd.read_csv(base_path + "Modulos.csv")

df_modulos = df_modulos.drop_duplicates(subset=["codigo"])

df_modulos.rename(columns={"codigo": "modulo_id"}, inplace=True)

df_modulos.to_csv("Dimensiones/dim_modulo.csv", index=False, sep=";")

# ------------------------------
# 4. DIMENSION GRUPO
# ------------------------------

df_grupos = pd.read_csv(base_path + "Grupos.csv")

df_grupos = df_grupos.drop_duplicates(subset=["codigo"])

df_grupos.rename(columns={"codigo": "grupo_id"}, inplace=True)

df_grupos.to_csv("Dimensiones/dim_grupo.csv", index=False, sep=";")

# ------------------------------
# 5. DIMENSION EVALUACION (SE SACA DE CALIFICACIONES)
# ------------------------------

df_calificaciones = pd.read_csv(base_path + "Calificaciones.csv")

df_eval = df_calificaciones.drop_duplicates(subset=["evaluacion"])

df_eval.to_csv("Dimensiones/dim_evaluacion.csv", index=False, sep=";")

print("Dimensiones creadas correctamente.")
