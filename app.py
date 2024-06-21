# app.py

from flask import Flask
from config import Config  
from config import db 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

app = Flask(__name__)
app.config.from_object(Config)  
db = SQLAlchemy(app)  
migrate = Migrate(app, db)  

# Définissez vos routes et d'autres configurations ici

if __name__ == '__main__':
    app.run(debug=True)
