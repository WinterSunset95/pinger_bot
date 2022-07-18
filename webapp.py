# Do not touch this file 

from flask import Flask
from threading import Thread
from time import sleep
import requests
from replit import db

app = Flask("")

@app.route("/")
def home():
  return ("Hello. This server is alive!")
def run():
  app.run(host="0.0.0.0", port=8080)
def loop():
  while True:
    sleep(120)
    try:
      db['minutes'] += 2
    except:
      db['minutes'] = 0
    requests.get("https://pingerbot.winter95.repl.co")

def keep_alive():
  l = Thread(target=loop)
  t = Thread(target=run)
  l.start()
  t.start()