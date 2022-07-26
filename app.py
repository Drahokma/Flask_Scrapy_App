import subprocess
import os
import psycopg2
from datetime import datetime
from flask import Flask, render_template, request
from PropertyScrap.settings import DATABASE_URL


app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn
    
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/scrape')
def scrape():
    """
    Run spider in another process and store items in file. Simply issue command:

    > scrapy crawl spidername -o "output.json"

    wait for  this command to finish, and read output.json to client.
    """
    now = datetime.now()
    date_time = now.strftime("%m-%d-%Y_%H-%M-%S")
    # /scrape?filename=jsonfilename
    filename = request.args.get('filename', default='output_'+date_time, type=str)
    output_json = filename + '.json'
    spider_name = "property"
    subprocess.check_output(['scrapy', 'crawl', spider_name, "-o", 'output/' + output_json])
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM items;')
    items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('scrape.html', items=items)



if __name__ == '__main__':
    app.run(debug=True)
