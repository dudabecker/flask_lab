from flask import Flask, render_template
from outro import nome

app = Flask(__name__)  # sao 2 underlines antes e 2 depois

noticias = [
    {
        "titulo": "Cadelinha assina projeto de Lei",
        "texto": "Cadela Many tem a doença leishmaniose visceral canina e foi levada para dar visibilidade ao tema. Projeto prevê que tutores de baixa renda recebam medicamento para tratar o cão de estimação que estiver com a moléstia."
    },
    {
        "titulo": "Musk Perde 50 bilhões",
        "texto": "Texto texto texto"
    }
]

# 1 rota -> meusite.com.br/ meusite.com.br/contatos
# 2 funcao


@app.route("/home/")
@app.route("/")
def index():
    return render_template("index.html", notic=noticias)


@app.route("/contato/")
def contato():
    return "contatos"


# 3 rodar nossa aplicacao
if __name__ == "__main__":
    app.run(debug=True)
