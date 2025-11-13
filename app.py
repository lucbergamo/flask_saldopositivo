from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///saldopositivo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class gastos_var(db.Model):
    __tablename__ = 'gastos_var'
    id = db.Column(db.Integer, primary_key=True)
    gasto = db.Column(db.String(70))
    data = db.Column(db.Date,nullable=False)
    valor = db.Column(db.Numeric(10,2))
    categoria = db.Column(db.String(40))

    def __init__(self,gasto, data, valor,categoria):
        self.gasto = gasto
        self.data = data
        self.valor = valor
        self.categoria = categoria

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gastos_var', methods=['POST', 'GET'])
def gastos_var():
    gasto = request.form['gasto']
    data = request.form['data']
    valor = request.form['valor']
    categoria = request.form['categoria']

    return render_template('gastos_var.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)