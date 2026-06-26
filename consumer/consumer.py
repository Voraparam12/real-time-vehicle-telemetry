import json
import os
import sys

import pandas as pd
from kafka import KafkaConsumer
from sqlalchemy import create_engine

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

engine = create_engine(
    "postgresql+psycopg2://postgres:Param@localhost:5432/vehicle_telemetry"
)
with engine.connect() as conn:
    print("Database connection successful")
consumer = KafkaConsumer(
    'vehicle_telemetry',
    bootstrap_servers='127.0.0.1:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='vehicle-group-v3'
)

print("Consumer started...")

for message in consumer:
    try:
        data = message.value
        
        print("Received:", data)

        df = pd.DataFrame([data])

        df.to_sql(
             'vehicle_telemetry',
            engine,
            if_exists='append',
            index=False
        )

        print(f"Inserted: {data}")
    
    except Exception as e:
        print("Error:", e)