<h1> 👾 CH4VES_BOT 👾</h1>
<h2>  🟢  Sistema feito em Python com flask   </h2>
<h2>  🟢  Sistema de pesquisa com consultas no banco de dados do WIKIPEDIA   </h2>

<h1> 🛠️ Funcionalidades -> </h1>
<h2>🟢  Pergunte o que quisers</h2>
<h2>🟢  codigo Gratuito para replicação e facil de entender</h2>
<h2>🟢  Sistema gratuito para implementação e uso</h2>

<h2>💻 SISTEMA ></h2>
<h2>🟢 https://chavesbot.onrender.com </h2>
<h2> Este é um código Python que cria um servidor web usando o framework Flask e permite que os usuários façam perguntas e obtenham respostas da Wikipedia. Vou explicar as funcionalidades deste código em detalhes:

<h2> Importação de Bibliotecas:</h2>

<h2>wikipedia: Importa a biblioteca Wikipedia API, que permite realizar pesquisas na Wikipedia.
Flask: Importa a biblioteca Flask, um framework para criar aplicativos da web.
render_template, request, redirect, session, e jsonify: Importa classes e funções do Flask para renderizar templates HTML, manipular solicitações HTTP, redirecionar páginas, gerenciar sessões e serializar/desserializar JSON.
datetime: Importa a classe datetime para trabalhar com datas e horários.
requests: Importa a biblioteca requests para fazer solicitações HTTP, usada para obter informações de geolocalização.
Instância do Aplicativo Flask:</h2>

<h2>app = Flask(__name__): Cria uma instância do aplicativo Flask.</h2>
<h2>Chave Secreta de Sessão:</h2>

<h2>app.secret_key = 'tiodino': Define uma chave secreta para a sessão do Flask. Isso é usado para proteger os dados da sessão.</h2>
<h2>Configuração da Língua da Wikipedia:</h2>

<h2>wikipedia.set_lang('pt'): Configura o idioma da Wikipedia para português.</h2>
<h2>Registro de Acessos:</h2>

<h2>access_logs: Uma lista que será usada para rastrear os acessos aos recursos do aplicativo.</h2>
<h2>AccessLog: Uma classe que representa um registro de acesso, com atributos como endereço IP, carimbo de data/hora e localização.</h2>
<h2>Rota '/resposta':</h2>

<h2>@app.route('/resposta'): Define uma rota que responde a solicitações GET para '/resposta'.</h2>
<h2>index(): Uma função que é chamada quando essa rota é acessada. Ela obtém uma pergunta da sessão, pesquisa na Wikipedia e exibe uma resposta.</h2>
<h2>Rota '/' e '/pergunta':</h2>

<h2>@app.route('/') e @app.route('/pergunta', methods=['POST']): Define rotas para a página inicial e para receber perguntas dos usuários via POST.</h2>
<h2>perguntass(): Função que exibe a página inicial com um formulário para fazer perguntas.</h2>
<h2>criar(): Função que é chamada quando um formulário de pergunta é enviado. Ela registra o acesso, obtém informações de geolocalização e redireciona para a rota '/resposta'.</h2>
<h2>Rota '/access_logs':</h2>

<h2>@app.route('/access_logs', methods=['GET']): Define uma rota para visualizar os registros de acesso.</h2>
<h2>get_access_logs(): Função que transforma os registros de acesso em um formato que pode ser renderizado em uma página HTML.</h2>
<h2>Execução do Aplicativo Flask:</h2>

<h2>if __name__ == "__main__":: Verifica se o script está sendo executado diretamente.</h2>
<h2>app.run(debug=True): Inicia o aplicativo Flask em modo de depuração.</h2>
<h2>Em resumo, este código cria um aplicativo da web Flask que permite que os usuários façam perguntas e obtenham respostas da Wikipedia. Ele também rastreia os acessos dos usuários, registra informações de geolocalização e fornece uma visualização dos registros de acesso.</h2>
