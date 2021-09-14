from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Página Principal</h1><p>Acesse nossa página de detalhes <a href='detalhes' >Link para Detalhes</a><p>"

@app.route("/detalhes")
def detalhes():
    return "<h1>Página de detalhes<p><a href='/' >Link para Página Inicial</a><p><h1>"

if __name__ == '__main__':
    app.run(debug=True)

