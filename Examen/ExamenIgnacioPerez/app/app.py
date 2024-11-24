from flask import Flask,request,render_template
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/ejercicio1', methods=['GET','POST'])
def formularioE1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        numTarros = int(request.form['numTarros'])
        pctDescuento=0
        if 18<=edad<=30:
            pctDescuento=0.15
        elif edad>30:
            pctDescuento=0.25
        total = 9000 * numTarros
        descuento=pctDescuento*total
        pagoFinal=total-descuento
        return render_template('ejercicio1.html', nombre=nombre,pagoFinal=pagoFinal, total=total,descuento=descuento)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET','POST'])
def formularioE2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        if nombre=="juan" and contrasena=="admin":
            return render_template('ejercicio2.html', nombre=nombre, tipoUsuario="Administrador")
        elif nombre=="pepe" and contrasena=="user":
            return render_template('ejercicio2.html', nombre=nombre, tipoUsuario="Usuario")
        else:
            return render_template('ejercicio2.html', error=True)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)