
# config.py

from flask_sqlalchemy import SQLAlchemy

# Crée une instance de SQLAlchemy sans l'initialiser avec l'application Flask
db = SQLAlchemy()

# Configuration de l'application Flask
class Config:
    DEBUG = True  # Activer le mode debug
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mdp1@localhost/fixitbot'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Désactiver le suivi des modifications de SQLAlchemy
