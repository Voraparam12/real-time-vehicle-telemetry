import json
import time
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from kafka import KafkaProducer
from data_generator.generate_data import generate_vehicle_data

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Producer started...")

while True:
    data = generate_vehicle_data()

    future = producer.send(
        'vehicle_telemetry',
        value=data
    )
    producer.flush()

    print(f"Sent: {data}")
    

    time.sleep(1)