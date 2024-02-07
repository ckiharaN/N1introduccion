## importamos flask
from flask import Flask
app=Flask(__name__)


## Definimos la ruta principal
@app.route("/")
def HolaFlask():
    return "<h1>¡Hola Flask!</h1> <hr>"

@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1,nota2,nota3):
    resultado = (nota1*30)/100 + (nota2*30)/100 + (nota3*40)/100
    return f"<h1>El resultado es: {resultado}</h1><hr>"                                                                                   
  
    
##http://127.0.0.1:5000/notas/6.7/3.4/6.3
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad<18:
        R="menor de edad" 
    elif(edad<60):
        R="Adulto"
    else:
        R="Adulto mayor"
    return f"<h1>La persona es: {R} </h1> <hr>"

    ##fin del codigo edades


##comienzo del codigo arreglos
import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0,columnas=0,filas=0):
    if filas==0:
        arreglo=np.random.randint(valores, size=columnas)
    
    else:
        arreglo=np.random.randint(valores, size=(filas,columnas))
        
    return f"<h1>El arreglo aleatorio es: {arreglo}</h1> <hr>"



if __name__=='__main__':
    ##El valor true indica que la app se deja en modo debug
    app.run(debug=True)
