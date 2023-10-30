import wikipedia
from flask import Flask, render_template, request, redirect, session, jsonify
from datetime import datetime
import requests

app = Flask(__name__)
app.secret_key = 'tiodino'
wikipedia.set_lang('pt')


# Lista para rastrear os acessos que foi criado na rota para verificar as pessoas que acessaram

access_logs = []

class AccessLog:
    def __init__(self, ip_address, timestamp, location):
        self.ip_address = ip_address
        self.timestamp = timestamp
        self.location = location


@app.route('/resposta')
def index():
    pergunta = session.get('pergunta', '')
    resposta = wikipedia.search(pergunta, results=3)
    resumo = "Não foi possivel encontrar sua Duvida em meu Banco de Dados, Tente ser mais especifico ou seja mais direto ao ponto!"


    if resposta:
        try:
            resumo = wikipedia.summary(resposta[0], sentences=10)
        except wikipedia.exceptions.DisambiguationError as e:
            resumo = "Múltiplas opções encontradas. Por favor, especifique sua pergunta de forma mais precisa."
        except wikipedia.exceptions.PageError as e:
            resumo = "Nenhuma informação encontrada para esta pergunta."


    return render_template('resposta.html', resposta=resumo, pergunta=pergunta)

@app.route('/')
def perguntass():
    return render_template('inicio.html')

@app.route('/pergunta', methods=['POST'])
def criar():
    pergunta = request.form['pergunta']
    session['pergunta'] = pergunta
    # Registrar o acesso
    if 'X-Forwarded-For' in request.headers:
        ip_address = request.headers['X-Forwarded-For']
    else:
        ip_address = request.remote_addr
    # Obter informações de geolocalização usando o serviço "ipinfo.io"
    geo_info = requests.get(f"https://ipinfo.io/{ip_address}/json").json()
    location = geo_info.get("city", "Desconhecida")  # Pode usar outros campos como "country" ou "region" conforme necessário

    access_logs.append(AccessLog(ip_address, datetime.now(), location))
    if pergunta == '':
        return redirect('/')
    else:
        return redirect('/resposta')


@app.route('/access_logs', methods=['GET'])
def get_access_logs():
    # Rota para visualizar os registros de acesso
    logs = [{"ip_address": log.ip_address, "timestamp": log.timestamp.strftime("%Y-%m-%d %H:%M:%S"), "location": log.location} for log in access_logs]
    return render_template('access_logs.html', logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
