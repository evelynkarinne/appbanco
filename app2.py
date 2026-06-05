from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, Colaborador, Venda
from flask import render_template

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    return {"mensagem": "Projeto Banco de Dados"}

@app.route("/colaboradores")
def listar_colaboradores():

    colaboradores = Colaborador.query.all()

    return [
        colaborador.to_dict()
        for colaborador in colaboradores
    ]

@app.route("/vendas")
def listar_vendas():

    vendas = Venda.query.all()

    return [
        venda.to_dict()
        for venda in vendas
    ]

@app.route("/relatorio-vendas")
def relatorio_vendas():

    vendas = Venda.query.all()

    resultado = []

    for venda in vendas:
        resultado.append({
            "codigo": venda.codigo,
            "vendedor": venda.colaborador.nome,
            "cidade": venda.colaborador.cidade,
            "data_venda": venda.data_venda.isoformat() if venda.data_venda else None,
            "valor": float(venda.valor)
        })

    return resultado

if __name__ == "__main__":
    app.run(debug=True)


