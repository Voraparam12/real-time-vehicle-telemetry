import os
import sys
import time

import pandas as pd
from sqlalchemy import create_engine

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_generator.generate_data import generate_vehicle_data

engine = create_engine(
    "postgresql+psycopg2://postgres:Param@localhost:5432/vehicle_telemetry"
)

print("Starting ETL pipeline...")

while True:
    data = generate_vehicle_data()

    df = pd.DataFrame([data])

    df.to_sql(
        "vehicle_telemetry",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Inserted: {data}")

    time.sleep(1)