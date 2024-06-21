from flask import request, jsonify
from app import app, db
from models import Utilisateur, Conversation, Message, Erreur, Solution, Outil

# Routes pour Utilisateurs
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = Utilisateur(nom=data['nom'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Utilisateur créé avec succès'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = Utilisateur.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = Utilisateur.query.get_or_404(id)
    return jsonify(user.to_dict())

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = Utilisateur.query.get_or_404(id)
    user.nom = data.get('nom', user.nom)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify({'message': 'Utilisateur mis à jour avec succès'})

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = Utilisateur.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Utilisateur supprimé avec succès'})

# Routes pour Conversations
@app.route('/conversations', methods=['POST'])
def create_conversation():
    data = request.get_json()
    new_conversation = Conversation(utilisateur_id=data['utilisateur_id'])
    db.session.add(new_conversation)
    db.session.commit()
    return jsonify({'message': 'Conversation créée avec succès'}), 201

@app.route('/conversations', methods=['GET'])
def get_conversations():
    conversations = Conversation.query.all()
    return jsonify([conversation.to_dict() for conversation in conversations])

@app.route('/conversations/<int:id>', methods=['GET'])
def get_conversation(id):
    conversation = Conversation.query.get_or_404(id)
    return jsonify(conversation.to_dict())

@app.route('/conversations/<int:id>', methods=['DELETE'])
def delete_conversation(id):
    conversation = Conversation.query.get_or_404(id)
    db.session.delete(conversation)
    db.session.commit()
    return jsonify({'message': 'Conversation supprimée avec succès'})

# Routes pour Messages
@app.route('/messages', methods=['POST'])
def create_message():
    data = request.get_json()
    new_message = Message(conversation_id=data['conversation_id'], sender=data['sender'], message=data['message'])
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'message': 'Message créé avec succès'}), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([message.to_dict() for message in messages])

@app.route('/messages/<int:id>', methods=['GET'])
def get_message(id):
    message = Message.query.get_or_404(id)
    return jsonify(message.to_dict())

@app.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    message = Message.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    return jsonify({'message': 'Message supprimé avec succès'})

# Routes pour Erreurs
@app.route('/errors', methods=['POST'])
def create_error():
    data = request.get_json()
    new_error = Erreur(description=data['description'])
    db.session.add(new_error)
    db.session.commit()
    return jsonify({'message': 'Erreur créée avec succès'}), 201

@app.route('/errors', methods=['GET'])
def get_errors():
    errors = Erreur.query.all()
    return jsonify([error.to_dict() for error in errors])

@app.route('/errors/<int:id>', methods=['GET'])
def get_error(id):
    error = Erreur.query.get_or_404(id)
    return jsonify(error.to_dict())

@app.route('/errors/<int:id>', methods=['DELETE'])
def delete_error(id):
    error = Erreur.query.get_or_404(id)
    db.session.delete(error)
    db.session.commit()
    return jsonify({'message': 'Erreur supprimée avec succès'})

# Routes pour Solutions
@app.route('/solutions', methods=['POST'])
def create_solution():
    data = request.get_json()
    new_solution = Solution(description=data['description'])
    db.session.add(new_solution)
    db.session.commit()
    return jsonify({'message': 'Solution créée avec succès'}), 201

@app.route('/solutions', methods=['GET'])
def get_solutions():
    solutions = Solution.query.all()
    return jsonify([solution.to_dict() for solution in solutions])

@app.route('/solutions/<int:id>', methods=['GET'])
def get_solution(id):
    solution = Solution.query.get_or_404(id)
    return jsonify(solution.to_dict())

@app.route('/solutions/<int:id>', methods=['DELETE'])
def delete_solution(id):
    solution = Solution.query.get_or_404(id)
    db.session.delete(solution)
    db.session.commit()
    return jsonify({'message': 'Solution supprimée avec succès'})

# Routes pour Outils
@app.route('/tools', methods=['POST'])
def create_tool():
    data = request.get_json()
    new_tool = Outil(nom=data['nom'], description=data.get('description'))
    db.session.add(new_tool)
    db.session.commit()
    return jsonify({'message': 'Outil créé avec succès'}), 201

@app.route('/tools', methods=['GET'])
def get_tools():
    tools = Outil.query.all()
    return jsonify([tool.to_dict() for tool in tools])

@app.route('/tools/<int:id>', methods=['GET'])
def get_tool(id):
    tool = Outil.query.get_or_404(id)
    return jsonify(tool.to_dict())

@app.route('/tools/<int:id>', methods=['DELETE'])
def delete_tool(id):
    tool = Outil.query.get_or_404(id)
    db.session.delete(tool)
    db.session.commit()
    return jsonify({'message': 'Outil supprimé avec succès'})

