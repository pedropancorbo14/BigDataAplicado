# Practica 2
## 1. Configuración del entorno FIWARE:

services:
  orion:
    image: fiware/orion
    container_name: orion
    ports:
      - "1026:1026"
    command: -logLevel DEBUG -noCache -dbURI mongodb://mongo:27017
    environment:
     - MONGO_HOST=mongo
    depends_on:
      - mongo

  mongo:
    image: mongo:4.4
    container_name: mongo
    ports:
      - "27017:27017"
    volumes:
      - mongodata:/data/db

  quantumleap:
    image:  fiware/quantum-leap
    container_name: quatum-leap
    ports:
      - "8668:8668"
    depends_on:
      - mongo
      - orion
      - crate
    environment:
      - CRATE_HOST=crate

  crate:
    image: crate:5.0.0
    container_name: crate
    ports:
      - "4200:4200"
      - "5432:5432"
    command: ["crate", "-Ccluster.name=crate-cluster", "-Chttp.cors.enabled=true", "-Chttp.cors.allow-origin=*"]
    volumes:
      - cratedata:/data

  grafana:
    image: grafana/grafana
    container_name: grafana
    ports:
      - "3000:3000"
    environment:
      - "GF_SECURITY_ADMIN_PASSWORD=admin"  # Cambia según tus preferencias
    depends_on:
      - quantumleap
volumes:
    mongodata:
    cratedata:


##  2. Creación de las 3 entidades:

Llamada a la api de orion: http://localhost:1026/v2/entities

Los Json:

{
    "id": "Sensor_TempHum_1",
    "type": "Temperatura_y_humedad",
    "location": { "type": "String", "value": "Puerta" },
    "temperature": { "type": "Float", "value": 20 },
    "humidity": { "type": "Float", "value": 80 },
    "created_at": { "type": "Datetime", "value": "2024-04-02 20:22:44" },
    "updated_at": { "type": "Datetime", "value": "2024-04-02 20:22:44" }
}
{
    "id": "Sensor_TempHum_2",
    "type": "Temperatura_y_humedad",
    "location": { "type": "String", "value": "Sala principal" },
    "temperature": { "type": "Float", "value": 22.5 },
    "humidity": { "type": "Float", "value": 65 },
    "created_at": { "type": "Datetime", "value": "2024-04-02 20:25:10" },
    "updated_at": { "type": "Datetime", "value": "2024-04-02 20:25:10" }
}
{
    "id": "Sensor_TempHum_3",
    "type": "Temperatura_y_humedad",
    "location": { "type": "String", "value": "Almacen" },
    "temperature": { "type": "Float", "value": 18.7 },
    "humidity": { "type": "Float", "value": 72 },
    "created_at": { "type": "Datetime", "value": "2024-04-02 20:30:27" },
    "updated_at": { "type": "Datetime", "value": "2024-04-02 20:30:27" }
}

## 3. Creación de una suscripción:

Llamada a la api de orion: http://localhost:1026/v2/subscriptions

Json:

{
    "description": "Suscripcion QuantumLeap Temperatura y Humedad",
    "subject": {
        "entities": [
            {
                "idPattern": ".*",
                "type": "Temperatura_y_humedad"
            }
        ],
        "condition": {
            "attrs": [
                "temperature",
                "humidity"
            ]
        }
    },
    "notification": {
        "attrs": [
            "id",
            "type",
            "location",
            "temperature",
            "humidity",
            "created_at",
            "updated_at"
        ],
        "http": {
            "url": "http://quantumleap:8668/v2/notify"
        },
        "metadata": [
            "dateCreated",
            "dateModified"
        ]
    }
}

## 4. Carga de datos:

Archivo consultas.py

## 5. Consulta Mongodb

./Images/Consulta1.png
./Images/Consulta2.png
./Images/Consulta3.png