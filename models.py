from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Colaborador(db.Model):
    __tablename__ = "colaboradores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(30))
    salario = db.Column(db.Numeric(10, 2))
    email = db.Column(db.String(40))

    vendas = db.relationship(
        "Venda",
        backref="colaborador",
        lazy=True,
        cascade="all, delete"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cidade": self.cidade,
            "salario": float(self.salario) if self.salario else None,
            "email": self.email
        }


class Venda(db.Model):
    __tablename__ = "vendas"

    codigo = db.Column(db.Integer, primary_key=True)
    
    vendedor_id = db.Column(
        db.Integer,
        db.ForeignKey("colaboradores.id"),
        nullable=False
    )

    data_venda = db.Column(db.Date)
    valor = db.Column(db.Numeric(10, 2), nullable=False)

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "vendedor_id": self.vendedor_id,
            "data_venda": self.data_venda.isoformat() if self.data_venda else None,
            "valor": float(self.valor)
        }