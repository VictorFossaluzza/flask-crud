from flask import Flask, render_template, request, url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'DATABASE_CONNECTION_STRING'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Aluno(db.Model):
    __tablename__ = "VictorFossaluzza"
    ra = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50))
    logradouro = db.Column(db.String(50))
    numero = db.Column(db.String(5))
    cep = db.Column(db.String(10))
    complemento = db.Column(db.String(20))

    def __init__(self, ra, nome, email, logradouro, numero, cep, complemento):
        self.ra = ra
        self.nome = nome
        self.email = email
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.complemento = complemento


@app.route('/')
def index():
    alunos = Aluno.query.all()
    return render_template("index.html", alunos=alunos)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        ra = request.form['ra']
        nome = request.form['nome']
        email = request.form['email']
        logradouro = request.form['logradouro']
        numero = request.form['numero']
        cep = request.form['cep']
        complemento = request.form['complemento']
        
        aluno = Aluno(ra,nome,email,logradouro,numero,cep,complemento)
        db.session.add(aluno)
        db.session.commit()
        
        flash("Aluno inserido com sucesso")
        
        return redirect(url_for("index"))
        
@app.route('/update',methods=['GET','POST'])
def update():
    if request.method == 'POST':
        aluno = Aluno.query.get(request.form.get('ra'))
        aluno.ra = request.form['ra']
        aluno.nome = request.form['nome']
        aluno.email = request.form['email']
        aluno.logradouro = request.form['logradouro']
        aluno.numero = request.form['numero']
        aluno.cep = request.form['cep']
        aluno.complemento = request.form['complemento']
        
        db.session.commit()
        flash("O Aluno foi atualizado")
        
        return redirect(url_for('index'))
    
@app.route('/delete/<int:id>')
def delete(id):
    aluno = Aluno.query.get(id)
    db.session.delete(aluno)
    db.session.commit() 
    flash('O Aluno foi deletado com sucesso!')
    return redirect(url_for('index'))
        


if __name__ == "__main__":
    app.run(debug=True)
