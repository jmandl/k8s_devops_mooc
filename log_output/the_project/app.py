import uuid
import time
from datetime import datetime, timezone

def get_utc_timestamp():
    now = datetime.now(timezone.utc)
    return now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

def generate_uuid_loop():
    return uuid.uuid4()

if __name__ == "__main__": 
    while True:
        timestamp = get_utc_timestamp()
        new_uuid = generate_uuid_loop()
        print(f"{timestamp}: {new_uuid}")
        time.sleep(5)