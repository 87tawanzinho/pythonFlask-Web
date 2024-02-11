from flask import Flask
from routes.home import home_route


app = Flask(__name__) 


app.register_blueprint(home_route) # pega a rota 

app.run(debug=True)