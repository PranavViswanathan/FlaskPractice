from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])

def index():
    
    req = requests.get("https://cat-fact.herokuapp.com/facts")
    data = req.content
    json_data = json.loads(data)
    return render_template('index.html', data = json_data)
