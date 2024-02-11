from flask import Flask, url_for, render_template


app = Flask(__name__) 





#rotas
@app.route('/', methods=['GET'])
def hello_world():
    titulo = "Gestão de Usuários"

    usuarios = [
        {"nome": "Guilherme", "membro_ativo": True},
        {"nome": "Maria", "membro_ativo": False}
    ]   
    return render_template("index.html", titulo=titulo, usuarios=usuarios)


@app.route('/sobre', methods=['GET'])
def sayAboutMe():
    return f"<a href='{ url_for('hello_world') }'>click aqui</a>"





app.run(debug=True)