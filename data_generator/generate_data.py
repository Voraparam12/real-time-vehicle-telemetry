import random
from datetime import datetime
from faker import Faker

fake = Faker()

def generate_vehicle_data():

    return {
        "vehicle_id": f"VH-{random.randint(1, 100)}",
        "event_time": datetime.now().isoformat(),
        "speed": round(random.uniform(0, 140), 2),
        "engine_temperature": round(random.uniform(70, 120), 2),
        "fuel_level": round(random.uniform(5, 100), 2),
        "battery_voltage": round(random.uniform(11.5, 14.5), 2),
        "latitude": float(fake.latitude()),
        "longitude": float(fake.longitude())
    }