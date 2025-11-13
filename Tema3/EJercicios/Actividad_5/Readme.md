# DATA_CATALOG

| Nombre del Dataset      | Capa  | Ubicación / Ruta                                                  | Descripción                            | Esquema                                               | Calidad | Actualización | Responsable               |
|-------------------------|-------|--------------------------------------------------------------------|------------------------------------------|-------------------------------------------------------|---------|---------------|----------------------------|
| calificaciones_bronce   | Bronce| /Datos_crudos(Bronce)/2025/1Eva/calificaciones.csv                | Datos originales sin limpiar             | alumno, asignatura, nota, fecha                       | Baja    | Diaria        | Ingesta (NiFi)            |
| calificaciones_plata    | Plata | /Procesados(Plata)/2025/1Eva/calificaciones_clean.parquet         | Datos limpios y validados                | alumno, asignatura, nota_normalizada, fecha           | Media   | Diaria        | Ingeniero de Datos        |
| calificaciones_oro      | Oro   | /Analizados(Oro)/2025/1Eva/calificaciones_agregadas.parquet       | Datos agregados para análisis BI         | alumno, media_notas, asignatura, media_asignatura     | Alta    | Diaria        | Analista BI               |


# DATA_LINEAGE

| Etapa / Fichero                  | Origen                                                     | Transformaciones Aplicadas                                              | Destino                                                       | Responsable          |
|----------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------|-----------------------|
| Ingesta CSV                      | calificaciones.csv (fuente externa)                        | Sin transformaciones                                                     | /Datos_crudos(Bronce)/2025/1Eva/calificaciones.csv            | NiFi / Ingesta       |
| Transformación Plata (1)         | /Datos_crudos(Bronce)/2025/1Eva/calificaciones.csv         | Convertir nota a número · Limpiar no válidos · Normalizar fecha         | /Procesados(Plata)/2025/1Eva/calificaciones_clean.parquet     | Ingeniero de Datos   |
| Transformación Plata (2)         | /Procesados(Plata)/2025/1Eva/calificaciones_clean.parquet  | Validar rango 0–10 · Imputar/eliminar nulos · Detectar duplicados       | /Procesados(Plata)/2025/1Eva/calificaciones_clean.parquet     | Ingeniero de Datos   |
| Agregación Oro                   | /Procesados(Plata)/2025/1Eva/calificaciones_clean.parquet  | Media por alumno · Media por asignatura · Preparación para BI           | /Analizados(Oro)/2025/1Eva/calificaciones_agregadas.parquet   | Analista BI          |
