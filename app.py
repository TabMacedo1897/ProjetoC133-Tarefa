from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    nome = "Kairo"
    idade = "14"
    return render_template('index.html', nome=nome, idade=idade)

@app.route("/pai")
def pagina_pai():
    nome_pai = "Nome do Pai"
    return render_template('pai.html', nome_pai=nome_pai)

@app.route("/mae")
def pagina_mae():
    nome_mae = "Nome da Mãe"
    return render_template('mae.html', nome_mae=nome_mae)

@app.route("/amigo")
def pagina_amigo():
    nome_amigo = "Nome do Amigo"
    return render_template('amigo.html', nome_amigo=nome_amigo)

# Adicione outras rotas conforme necessário

if __name__ == '__main__':
    app.run(debug=True)
