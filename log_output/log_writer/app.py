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
        try:
            with open('/app/log/log.txt', 'a') as f:
                f.write(str(new_uuid) + '\n')
        except IOError as e:
            print(f"An error occured while writing to the file: {e}")
        print(f"{timestamp}: {new_uuid}")
        time.sleep(5)