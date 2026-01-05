from flask import Flask, render_template, url_for

#inicializar o flask
app = Flask (__name__)

#rotas
@app.route('/')

def home(): 
 
    return render_template('index.html')
#usar url_for para links

@app.route('/caixa')
def pagina_caixa():
    return'''
            <b>
            <h1> </div>


'''
#pra por algum link usa: <a href= 'https: (link)'> (nome do que pode ser) </a>

if __name__ == '__main__':
#execução
    app.run(debug=True)

