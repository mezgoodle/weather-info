from flask import Flask, render_template, request
import sqlite3
from datetime import datetime as dt
import sqlite3

app = Flask(__name__)

# Index page, no args
app = Flask(__name__)
DBPATH = "./weather.db"

def get_latest():
    conn = sqlite3.connect(DBPATH)
    cur = conn.cursor()
    cur.execute("""
       select * from weather order by timestamp desc limit 1;
    """)
    row = cur.fetchall()[0]
    conn.close()
    ts = float(row[0])
    datetime = dt.fromtimestamp(ts).strftime("%d %b %H:%M:%S")
    temp = row[1]
    humidity = row[2]
    pressure = int(row[3] / 1.33322387415)
    light = row[4]
    return render_template("index.html", date=datetime, temp=temp, humidity=humidity, pressure=pressure, light=light)

@app.route('/')
def index():
    return get_latest()

# With debug=True, Flask server will auto-reload 
# when there are code changes
if __name__ == '__main__':
	app.run(port=5000, debug=True)  