from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_base64 = None

    if request.method == 'POST':
    nombre = request.form.get('nombre')
    direccion = request.form.get('direccion')
    visitante = request.form.get('visitante') 

    if nombre and direccion and visitante:
        data = f"Nombre residente: {nombre}\nDirección: {direccion}\nNombre visitante: {visitante}"
        img = qrcode.make(data)

            # Convertir imagen a base64
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            qr_base64 = f"data:image/png;base64,{img_base64}"

    return render_template('index.html', qr_code=qr_base64)

if __name__ == '__main__':
    app.run(debug=True)
