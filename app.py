import sqlite3
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import select
from wtforms import SelectField
from flask_wtf import FlaskForm


app = Flask(__name__, template_folder='templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///connectmei.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret"


db = SQLAlchemy(app)


class PessoaFisica(db.Model):
    __tablename__ = "pessoasfisicas"

    idpf= db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomepf = db.Column(db.String, nullable=False)
    cpf = db.Column(db.Integer, nullable=False, unique=True)
    sexopf = db.Column(db.String, nullable=False)
    emailpf = db.Column(db.String, nullable=False, unique=True)
    celularpf = db.Column(db.Integer, nullable=False, unique=True)
    logradouropf = db.Column(db.String, nullable=False)
    numeropf = db.Column(db.String, nullable=False)
    bairropf = db.Column(db.String, nullable=False)
    cidadepf = db.Column(db.String, nullable=False)
    ufpf = db.Column(db.String, nullable=False)
    ceppf = db.Column(db.Integer, nullable=False)
    senhapf = db.Column(db.String, nullable=False)

    def __init__(self, nomepf, cpf, sexopf, emailpf, celularpf, logradouropf, numeropf, bairropf, cidadepf, ufpf, ceppf, senhapf):
        self.nomepf = nomepf
        self.cpf = cpf
        self.sexopf = sexopf
        self.emailpf = emailpf
        self.celularpf = celularpf
        self.logradouropf = logradouropf
        self.numeropf = numeropf
        self.bairropf = bairropf
        self.cidadepf = cidadepf
        self.ufpf = ufpf
        self.ceppf = ceppf
        self.senhapf = senhapf

db.create_all()

 

class PessoaJuridica(db.Model):
    __tablename__ = "pessoasjuridicas"

    idpj = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomepj = db.Column(db.String, nullable=False)
    cnpj = db.Column(db.Integer, nullable=False, unique=True)
    profissao_nome = db.Column(db.String, nullable=False)
    emailpj = db.Column(db.String, nullable=False, unique=True)
    celularpj = db.Column(db.String, nullable=False, unique=True)
    logradouropj = db.Column(db.String, nullable=False)
    numeropj = db.Column(db.String, nullable=False)
    bairropj = db.Column(db.String, nullable=False)
    cidadepj = db.Column(db.String, nullable=False)
    ufpj = db.Column(db.String, nullable=False)
    ceppj = db.Column(db.Integer,nullable=False)  
    senhapj = db.Column(db.String, nullable=False)
   

    def __init__(self, nomepj, cnpj, profissao_nome, emailpj, celularpj, logradouropj, numeropj, bairropj, cidadepj, ufpj, ceppj, senhapj):
        self.nomepj = nomepj
        self.cnpj = cnpj
        self.profissao_nome = profissao_nome
        self.emailpj = emailpj
        self.celularpj = celularpj
        self.logradouropj = logradouropj
        self.numeropj = numeropj
        self.bairropj = bairropj
        self.cidadepj = cidadepj
        self.ufpj = ufpj
        self.ceppj = ceppj
        self.senhapj = senhapj
           
db.create_all()


class Form(FlaskForm):
    profissao_nome = SelectField('pessoasjuridicas', choices=[])


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")



@app.route("/politica")
def politica():
    return render_template("politicaPrivacidade.html") 
    

@app.route("/termos")
def termos():
    return render_template("termosServico.html") 



@app.route("/cadastrarpf")
def cadastrarpf():
    return render_template("cadastropf.html") 



@app.route("/cadastropf", methods=['GET', 'POST'])
def cadastropf():
    if request.method == "POST":
        nomepf = request.form.get("nomepf")
        cpf = request.form.get("cpf")
        sexopf = request.form.get("sexopf")
        emailpf = request.form.get("emailpf")
        celularpf = request.form.get("celularpf")
        logradouropf = request.form.get("logradouropf")
        numeropf = request.form.get("numeropf")
        bairropf = request.form.get("bairropf")
        cidadepf = request.form.get("cidadepf")
        ufpf = request.form.get("ufpf")
        ceppf = request.form.get("ceppf")
        senhapf = request.form.get("senhapf")

        if nomepf and cpf and sexopf and emailpf and celularpf and logradouropf and numeropf and bairropf and cidadepf and ufpf and ceppf and senhapf:
            pf = PessoaFisica(nomepf, cpf, sexopf, emailpf, celularpf, logradouropf, numeropf, bairropf, cidadepf, ufpf, ceppf, senhapf)
            db.session.add(pf)
            db.session.commit()

        return redirect(url_for("index"))
    return render_template('cadastropf.html')


        

@app.route("/listapf")
def listapf():
    pessoasfisicas = PessoaFisica.query.all()
    return render_template("listapf.html", pessoasfisicas=pessoasfisicas)



@app.route("/cadastrarpj")
def cadastrarpj():
    return render_template("cadastropj.html") 



@app.route("/cadastropj", methods=['GET', 'POST'])
def cadastropj():
    if request.method == "POST":
        nomepj = request.form.get("nomepj")
        cnpj = request.form.get("cnpj")
        profissao_nome = request.form.get("profissao_nome")
        emailpj = request.form.get("emailpj")
        celularpj = request.form.get("celularpj")
        logradouropj = request.form.get("logradouropj")
        numeropj = request.form.get("numeropj")
        bairropj = request.form.get("bairropj")
        cidadepj = request.form.get("cidadepj")
        ufpj = request.form.get("ufpj")
        ceppj = request.form.get("ceppj")
        senhapj = request.form.get("senhapj")

        if nomepj and cnpj and profissao_nome and emailpj  and celularpj and logradouropj and numeropj and bairropj and cidadepj and ufpj and ceppj and senhapj:
            pj = PessoaJuridica(nomepj, cnpj, profissao_nome, emailpj, celularpj, logradouropj, numeropj, bairropj, cidadepj, ufpj, ceppj, senhapj)
            db.session.add(pj)
            db.session.commit()

        return redirect(url_for("index"))
    return render_template('cadastropj.html')



@app.route("/listapj", methods=['GET'])
def listapj():
    pessoasjuridicas = PessoaJuridica.query.all()
    return render_template("listapj.html", pessoasjuridicas=pessoasjuridicas)
    


@app.route("/consultapj", methods=['GET'])
def consultapj():
    form = Form()
    form.profissao_nome.choices = [(profissao_nome.profissao_nome) for profissao_nome in PessoaJuridica.query.all()] 
    return render_template("consultapj.html", form=form)
  
    

@app.route('/deletepf/<int:idpf>')
def deletepf(idpf):
    pessoafisica = PessoaFisica.query.get(idpf)
    db.session.delete(pessoafisica)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/deletepj/<int:idpj>')
def deletepj(idpj):
    pessoajuridica = PessoaJuridica.query.get(idpj)
    db.session.delete(pessoajuridica)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/editpf/<int:idpf>', methods=['GET', 'POST'])
def editpf(idpf):
    pessoafisica = PessoaFisica.query.get(idpf)
    if request.method == "POST":
        pessoafisica.nomepf = request.form("nomepf")
        pessoafisica.cpf = request.form("cpf")
        pessoafisica.sexopf = request.form("sexopf")
        pessoafisica.emailpf = request.form("emailpf")
        pessoafisica.celularpf = request.form("celularpf")
        pessoafisica.logradouropf = request.form("logradouropf")
        pessoafisica.numeropf = request.form("numeropf")
        pessoafisica.bairropf = request.form("bairropf")
        pessoafisica.cidadepf = request.form("cidadepf")
        pessoafisica.ufpf = request.form("ufpf")
        pessoafisica.ceppf = request.form("ceppf")
        pessoafisica.senhapf = request.form("senhapf")
        if pessoafisica.nomepf or pessoafisica.cpf or pessoafisica.sexopf or pessoafisica.emailpf or pessoafisica.celularpf or pessoafisica.logradouropf or pessoafisica.numeropf or pessoafisica.bairropf or pessoafisica.cidadepf or pessoafisica.ufpf or pessoafisica.ceppf or pessoafisica.senhapf:
            db.session.add(pessoafisica)
            db.session.commit()

        return redirect(url_for("index"))

    return render_template('editpf.html', pessoafisica=pessoafisica)



@app.route('/editpj/<int:idpj>', methods=['GET', 'POST'])
def editpj(idpj):
    pessoajuridica = PessoaJuridica.query.get(idpj)
    if request.method == "POST":
        pessoajuridica.nomepj = request.form("nomepj")
        pessoajuridica.cnpj = request.form("cnpj")
        pessoajuridica.profissao_nome = request.form("profissao_nome")
        pessoajuridica.emailpj = request.form("emailpj")
        pessoajuridica.celularpj = request.form("celularpj")
        pessoajuridica.logradouropj = request.form("logradouropj")
        pessoajuridica.numeropj = request.form("numeropj")
        pessoajuridica.bairropj = request.form("bairropj")
        pessoajuridica.cidadepj = request.form("cidadepj")
        pessoajuridica.ufpj = request.form("ufpj")
        pessoajuridica.ceppj = request.form("ceppj")
        pessoajuridica.senhapj = request.form("senhapj")

        if  pessoajuridica.nomepj or pessoajuridica.cnpj or pessoajuridica.profissao_nome or pessoajuridica.emailpj  or pessoajuridica.celularpj or pessoajuridica.logradouropj or pessoajuridica.numeropj or pessoajuridica.bairropj or pessoajuridica.cidadepj or pessoajuridica.ufpj or pessoajuridica.ceppj or pessoajuridica.senhapj:
            db.session.add(pessoajuridica)
            db.session.commit()
        return redirect(url_for('index'))

    return render_template('editpj.html', pessoajuridica=pessoajuridica)



if __name__ == "__main__":
    app.run(debug=True)



