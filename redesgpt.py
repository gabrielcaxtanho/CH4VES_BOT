import wikipedia
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'tiodino'
wikipedia.set_lang('pt')

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
    if pergunta == '':
        return redirect('/')
    else:
        return redirect('/resposta')

if __name__ == "__main__":
    app.run(debug=True)
