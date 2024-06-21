from app import db

class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    mdp 

    def to_dict(self):
        return {
            'id': self.id,
            'utilisateur_id': self.nom,
            'timestamp': self.email
        }
    
class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'utilisateur_id': self.utilisateur_id,
            'timestamp': self.timestamp
        }

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'), nullable=False)
    sender = db.Column(db.Enum('user', 'bot'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return{
            'id': self.id,
            'conversation_id': self.conversation_id,
            'sender':self.sender,
            'message': self.message,
            'timestamp': self.timestamp,
        }

class Erreur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return{
            'id': self.id,
            'description' : self.description,
        }

class Solution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    
    def to_dict(self):
        return{
            'id':self.id,
            'description': self.description,
        }
    

class Outil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    def to_dict(self):
        return{
            'id': self.id,
            'description' : self.description,
        }

class solutionOutil(db.Model):
    erreur_id = db.Column(db.Integer, db.ForeignKey('erreur.id'), primary_key=True)
    outil_id = db.Column(db.Integer, db.ForeignKey('outil.id'), primary_key=True)

    def to_dict(self):
        return{
            'erreur_id': self.erreur_id,
            'outil_id':self.outil_id,
        }

class ErreurSolution(db.Model):
    erreur_id = db.Column(db.Integer, db.ForeignKey('erreur.id'), primary_key=True)
    solution_id = db.Column(db.Integer, db.ForeignKey('solution.id'), primary_key=True)

    def to_dict(self):
        return{
            'erreur_id':self.erreur_id,
            'outil_id':self.solution_id,
        }

class LogsInteraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), nullable=False)
    action = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return{
            'id':self.id,
            'utilisateur_id' : self.utilisateur_id,
            'action' : self.action,
            'timestamp': self.timestamp,
        }

class Requete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), nullable=False)
    requete = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return{
            'id': self.id,
            'utilisateur_id': self.utilisateur_id,
            'requete':self.requete,
            'timestamp' : self.timestamp,
        }
