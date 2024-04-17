from flask import Flask, render_template   

#creamos un objeto 
app = Flask(__name__)

@app.route('/')# ruta de inicio
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)# indicamos que nuestra aplicacion estra en mode de prueba

