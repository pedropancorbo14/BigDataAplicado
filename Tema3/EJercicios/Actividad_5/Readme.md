# DATA_CATALOG

| Nombre del Dataset     | Capa  | Ubicación / Ruta                                          | Descripción                                           | Esquema                                   | Calidad | Actualización | Responsable               |
|------------------------|-------|------------------------------------------------------------|-------------------------------------------------------|-------------------------------------------|---------|---------------|----------------------------|
| calificaciones_bronce | Bronce| /bronze/calificaciones/calificaciones.csv                 | Datos originales sin limpiar                          | alumno, asignatura, nota, fecha           | Baja    | Diaria        | Ingesta (NiFi)            |
| calificaciones_plata  | Plata | /silver/calificaciones/calificaciones_clean.parquet       | Datos limpios y validados                             | alumno, asignatura, nota_normalizada, fecha | Media   | Diaria        | Ingeniero de Datos        |
| calificaciones_oro    | Oro   | /gold/calificaciones/calificaciones_agregadas.parquet     | Datos agregados para análisis                         | alumno, media_notas, asignatura, media_asignatura | Alta | Diaria | Analista BI               |

# DATA_LINEAGE

| Etapa / Fichero                  | Origen                                 | Transformaciones Aplicadas                                                  | Destino                                               | Responsable          |
|----------------------------------|------------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------|-----------------------|
| Ingesta CSV                      | calificaciones.csv (fuente externa)      | Sin transformaciones                                                         | /bronze/calificaciones/calificaciones.csv             | NiFi / Ingesta       |
| Transformación Plata (1)         | Bronze                                   | Convertir nota a número · Limpiar no válidos · Normalizar fecha             | /silver/calificaciones_clean.parquet                  | Ingeniero de Datos   |
| Transformación Plata (2)         | Plata                                    | Validar rango 0–10 · Imputar/eliminar nulos · Detectar duplicados           | /silver/calificaciones_clean.parquet                  | Ingeniero de Datos   |
| Agregación Oro                   | Plata                                    | Media por alumno · Media por asignatura · Preparación para BI               | /gold/calificaciones_agregadas.parquet                | Analista BI          |
