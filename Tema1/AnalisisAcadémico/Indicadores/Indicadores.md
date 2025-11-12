Análisis Académico - Tarea 1: La Primera Inspección


Indicadores:

Preguntas: 

- ¿Cuál es el separador de columnas (coma , o punto y coma ; )?: ","

- ¿La primera fila contiene los nombres de las columnas (encabezados)? ¿Son claros?: 
    Sí y no, ya que tienen nombres muy genericos sobretodo las claves que relacionan

- Inspecciona visualmente las primeras 20-30 filas. ¿Ves valores que te parezcan extraños o que faltan (celdas vacías, "N/A", "s/d")?: 
    Faltan valores en las columnas Valor-T1, T2 y T3 en el archivo Indicadores_finales

- ¿Los formatos son consistentes? Por ejemplo, ¿las fechas están siempre como DD/MM/AAAA o a veces cambian?: 
    Sí

- Identifica las "claves" o "IDs" que podrían servir para relacionar unos ficheros con otros:  
    CLAVES
    Indicadores Finales
    Objetivos
    Lineas
    Procesos

    RELACIONES
    Objetivos (Objetivo PAA) - Indicadores Finales (Cod_PAA) 1-N
    Lineas (Linea) -  Objetivos (Linea) 1-N
    Procesos (Proceso) - Indicadores Finales (Cod_SQ) 1-N


