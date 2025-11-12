Análisis Académico - Tarea 1: La Primera Inspección

Datos 2022:

Preguntas:

- ¿Cuál es el separador de columnas (coma , o punto y coma ; )?: 
    ","

- ¿La primera fila contiene los nombres de las columnas (encabezados)? ¿Son claros?: 
    Sí y no, ya que tienen nombres muy genericos sobretodo las claves que relacionan

- Inspecciona visualmente las primeras 20-30 filas. ¿Ves valores que te parezcan extraños o que faltan (celdas vacías, "N/A", "s/d")?: 
    Faltan celdas de Código postal y tipo de matricula en alumnos.csv
    Faltan celdas de aula en Grupos.csv
    En Calificaciones.csv la celda contenido a veces es un int a veces un string (176 o CV0004)
    En Cursos.csv en las celdas nombre_cas y abreviatura hablan del nombre del grado, el tipo del grado(medio o superior) y los cursos de ese grado.


- ¿Los formatos son consistentes? Por ejemplo, ¿las fechas están siempre como DD/MM/AAAA o a veces cambian?: 
    Sí

- Identifica las "claves" o "IDs" que podrían servir para relacionar unos ficheros con otros:  
    CLAVES
    Calificaciones (evalución, alumno, contenido)
    Grupos(código)
    Alumnos (NIA)
    Módulos(curso, código)
    Horas(código)

    RELACIONES
    Cursos (código) - Alumnos (curso) 1-N
    Módulos (curso) - Cursos (codigo) N-1
    Horas (CODIGO) - Módulos (codigo) 1-N
    Cursos (codigo) - Calificaciones (curso) 1-N
    Calificaciones (alumno) - Alumnos (NIA) N-1
    Grupos (codigo) - Alumnos (grupo) 1-N
    Grupos (padre) - Grupos (codigo) 1-1 relación padre hijo en la misma tabla

    ESTRUCTURA
    Alumnos -> Cursos -> Módulos <- Horas
    Alumnos -> Calificaciones <- Cursos
    Alumnos -> Grupos
