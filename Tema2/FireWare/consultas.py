import requests
import random
import time

# Configuración
ORION_URL = "http://localhost:1026/v2/entities"  
ENTITIES = ["Sensor_TempHum_1", "Sensor_TempHum_2", "Sensor_TempHum_3"]

def updateEntitie(entidad_id):
    url = f"{ORION_URL}/{entidad_id}/attrs"
    
    payload = {
        "temperature": {
            "type": "Number",
            "value": round(random.uniform(18, 25), 1) 
        },
        "humidity": {
            "type": "Number",
            "value": round(random.uniform(60, 85), 1)
        },
        "updated_at": {
            "type": "DateTime",
            "value": time.strftime("%Y-%m-%dT%H:%M:%S")
        }
    }
    
    headers = {
        "Content-Type": "application/json"
    }

    ## Patch porque es un update
    response = requests.patch(url, json=payload, headers=headers)
    
    if response.status_code in [204, 200]:
        print(f"{entidad_id} actualizado correctamente.")
    else:
        print(f"Error actualizando {entidad_id}: {response.status_code}, {response.text}")

for i in range(400):
    print(f"\nActualización #{i+1}")
    for entidad in ENTITIES:
        updateEntitie(entidad)
    time.sleep(5)  # 5 segundo entre cada ciclo para no saturar Orion
