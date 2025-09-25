from flask import Flask
import os
import uuid
from datetime import datetime, timezone
import psycopg2

def db_connection():
    conn = psycopg2.connect(
        host="pingpongdb",
        database="mydb",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

conn = db_connection()
cur = conn.cursor()
try:
    cur.execute('CREATE TABLE pingpong (newvalue integer NOT NULL)')
    conn.commit()
except:
    print('table already exists!')
    
def generate_uuid_loop():
    return uuid.uuid4()

def get_utc_timestamp():
    now = datetime.now(timezone.utc)
    return now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

app = Flask(__name__)

PORT = int(os.getenv("PORT", 5000))

@app.route('/pingpong')
def index():
    timestamp = get_utc_timestamp()
    new_uuid = generate_uuid_loop()
    
    message = os.getenv("MESSAGE", "Message is null")

    try:
        with open('/app/static/file.txt', 'r') as f:
            message_in_file = f.read()
    except:
        message_in_file = 'no file in folder!'

    conn = db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pingpong')
    values = cur.fetchall()

    if values == []:
        counter = 0
    else:
        counter = values[-1][-1]
   
    counter += 1
    cur.execute('INSERT INTO pingpong (newvalue)''VALUES (%s)', (counter,))
    conn.commit()

    return f"""
    file content: {message_in_file}
    env variable: MESSAGE={message}
    {timestamp}: {new_uuid}.
    Ping / Pongs: {counter}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)