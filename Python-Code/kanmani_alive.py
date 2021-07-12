from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "!!KANMANI IS HERE TO HELP!!"
def run():
  app.run(host='0.0.0.0', port=8080)
def kanmani_alive():
  t = Thread(target=run)
  t.start()
