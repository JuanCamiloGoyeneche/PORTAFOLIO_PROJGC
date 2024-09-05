from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template ('index.html')

@app.route('/sobre')
def sobre():
    return render_template ('sobre.html')

@app.route('/cursos')
def cursos():
    return render_template ('cursos.html')

@app.route('/contacto')
def contacto():
    return render_template ('contacto.html')

@app.route('/mensaje', methods=['POST'])
def mensaje():
    if request.method == 'POST':
        nam = request.form['nombre']
        emm = request.form['email']
    return render_template ('mensaje.html', res=nam, ress=emm)



if __name__ == '__main__':
    app.run(debug=True)