import json
import requests
from flask import Flask, render_template

app = Flask(__name__)


def carregar_pokemons():
    with open('secrets.key') as file:
        psw = file.read()

    reqUrl = "https://alanfurquim.pythonanywhere.com/dados"

    headersList = {
        "x-api-key": psw
    }

    response = requests.request("GET", reqUrl,  headers=headersList, timeout=5).json()

    return {key: response[key] for key in sorted(response.keys(), key=int)}


@app.route('/')
def home():
    pokemons = carregar_pokemons()
    return render_template('index.html', pokemons=pokemons)


if __name__ == '__main__':
    app.run(debug=True)
