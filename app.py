from flask import Flask, render_template
from flask import send_file
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quienesSomos')
def quienesSomos():
    return render_template('quienesSomos.html')


@app.route('/resenas')
def resenas():
    return render_template('resenas.html')  # reseñas.html

@app.route('/demos')
def demos():
    return render_template('demos.html')


@app.route('/rompe-ladrillos')
def rompe_ladrillos():
    return render_template('rompeladrillos.html')


@app.route('/descargar-demo')
def descargar_demo():
    # Cambia la ruta al archivo correcto que pusiste en tu carpeta static
    return send_file("static/ST_QuickExchange_demo.rar", as_attachment=True)


@app.route("/ns")
def nuestros_servicios():
    return render_template("ns.html")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa el puerto de Render o 5000 por defecto
    app.run(debug=True, host='0.0.0.0', port=port)  # Cambia host a '0.0.0.0'
