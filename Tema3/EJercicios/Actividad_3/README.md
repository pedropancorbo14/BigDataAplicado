# README – Gobernanza y Calidad del Dato  
## Proyecto: *Análisis Académico* (Tarea 5)

Este documento forma parte del proyecto de Análisis Académico del Máster de Big Data y recoge los elementos de **Gobernanza del Dato** requeridos en la Tarea 5:

- **Catálogo de Datos (DATA_CATALOG.csv)**
- **Linaje del Dato (DATA_LINEAGE.csv)**

Ambos ficheros han sido generados siguiendo la arquitectura Medallion (Bronce → Plata → Oro) y documentan el ciclo completo del dato desde su origen hasta su explotación en la capa analítica.

---

# 📂 1. Arquitectura Medallion

La estructura del proyecto se basa en tres capas:

### 🟤 Capa Bronce (Datos_crudos)

Contiene los datos tal y como se reciben desde el sistema académico original:

- Calificaciones.csv  
- Cursos.csv  
- Alumnos.csv  
- Modulos.csv  
- Grupos.csv

### ⚪ Capa Plata (Datos_procesaods)

Aquí se aplican procesos de:

- Limpieza  
- Normalización  
- Eliminación de duplicados  
- Correcciones de tipos  
- Enriquecimiento (join entre curso ↔ nombre_cas)

### 🟡 Capa Oro (Analizados)

Contiene los datos listos para análisis:

- dim_alumno  
- dim_curso  
- dim_modulo  
- dim_grupo  
- dim_evaluacion  
- fact_media_calificaciones (CSV y Parquet por año/evaluación)

---

# 📘 2. Catálogo de Datos (DATA_CATALOG.csv)

El archivo define:

- Nombre del dataset  
- Capa (Bronce, Plata, Oro)  
- Origen  
- Formato  
- Columnas principales  
- Descripción  

---

# 🔄 3. Linaje del Dato (DATA_LINEAGE.csv)

Describe el flujo completo del dato:

- Origen del fichero  
- Transformaciones aplicadas (limpieza, validación, agregaciones)  
- Destino (Bronce, Plata, Oro)  
- Responsable de la transformación  

---

# 🏗️ 4. Flujo de Transformaciones Realizado

### Transformación 1  
Limpieza de Calificaciones → eliminación de duplicados, normalización de columnas, conversión de tipos.

### Transformación 2  
Enriquecimiento con Cursos.csv → merge curso ↔ codigo, añadir nombre_cas.

### Transformación 3  
Agrupación → alumno, curso, año, evaluación; cálculo de media_nota.

### Transformación 4  
Generación de outputs Oro → exportación de Parquet y CSV por año/evaluación.

### Transformación 5  
Creación de Dimensiones → deduplicación, renombrado de claves, exportación dim_*.

---

# 📊 5. Estructura del Directorio Oro

```
   Analizados/
      2022/
         Evaluaciones/
            1/
               fact_media_calificaciones.csv
               fact_media_calificaciones.parquet
            2/
               ...
```
