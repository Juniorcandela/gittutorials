from flask import Flask
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''

####WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the world of Junior Candela. Modificacion 1"

@app.route("/index")
def index():
    return "Welcome to index page."


if __name__ == "__main__":
    app.run(debug = True) # Esto reinicia el servidor para que se puedan aplicar los cambios del código en la página sin tener que reiniciar el server manualmente.
