from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route

app = Flask(__name__) 


app.register_blueprint(home_route) # pega a rota 
app.register_blueprint(cliente_route, url_prefix='/clientes') # pega a rota 

app.run(debug=True)