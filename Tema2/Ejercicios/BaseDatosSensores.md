# Base de datos de sensores

## Crea una base de datos llamada iot_data.

use iot_data

## Crea una colección llamada dispositivos.

db.createCollection("dispositivos")

## Inserta un documento en la colección dispositivos con la siguiente información:

db.dispositivos.insertOne(
{
    id_sensor: "temp01",
    tipo: "temperatura",
    ubicacion: "sala_servidores",
    valor_actual: 24.5,
    unidad: "celsius",
}
)

## Inserta dos nuevos documentos en la colección dispositivos: uno para un sensor de humedad (hum01) y otro para un sensor de CO2 (co201), con valores y ubicaciones que elijas.

db.dispositivos.insertMany([
{
    id_sensor: "hum01",
    tipo: "humedad",
    ubicacion: "sala_servidores",
    valor_actual: 50,
    unidad: "hr",
},
{
    id_sensor: "co201",
    tipo: "CO2",
    ubicacion: "sala_servidores",
    valor_actual: 400,
    unidad: "ppm",
}
])

## Busca y muestra solo los documentos de los sensores de tipo "temperatura".

db.dispositivos.find(
    {tipo:"temperatura"}
)


## Actualiza el valor actual del sensor con id_sensor: "temp01" a 25.8.

db.dispositivos.updateOne(
    {id_sensor:"temp01"},
    {$set:{valor_actual: 25.8}}
)

## Verifica que el valor se haya actualizado correctamente buscando el documento del sensor.

db.dispositivos.find(
    {id_sensor:"temp01"}
)

## Elimina el documento del sensor de CO2 (co201) de la colección.

db.dispositivos.deleteOne(
    {id_sensor:"co201"}
)

## Verifica que el documento ya no exista.

db.dispositivos.find(
    {id_sensor:"co201"}
)
