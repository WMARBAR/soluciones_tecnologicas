from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienesSomos.html')

@app.route('/servicios')
def servicios():
    return render_template('ns.html')

@app.route('/clientes')
def clientes():
    return render_template('resenas.html')

@app.route('/demos')
def demos():
    return render_template('demos.html')

@app.route('/rompeladrillos')
def rompeladrillos():
    return render_template('rompeladrillos.html')


# Rutas de compatibilidad por si ya las usabas
@app.route('/quienesSomos')
def quienes_somos_legacy():
    return render_template('quienesSomos.html')

@app.route('/ns')
def servicios_legacy():
    return render_template('ns.html')

@app.route('/resenas')
def clientes_legacy():
    return render_template('resenas.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)