from flask import Flask,render_template,request #utilizando mais ferramentas

app = Flask (__name__)

@app.route('/')#rota inicial
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST'])#segunda rota, que ira retorna apenas acesso negado e liberado
def login():
    user = request.form.get('user')
    passwprd = request.form.get('password')

    if user == "m4tos." and passwprd == "1234":
        return "Acesso liberado!👌"
    else: 
        return "Acesso negado!!😐😶‍🌫️"
    
if __name__ == '__main__':
    app.run("0.0.0.0", port=8000)








