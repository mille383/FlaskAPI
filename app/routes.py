from flask import jsonify
from flask import request
from app import app, db
from app.models import User

@app.route('/', methods=["GET"])
def get_api():
    
    return jsonify([u.to_dict() for u in User.query.all()])

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    """
    [GET] /api/product/<id>
    """
    return jsonify(User.query.get(id).to_dict())

@app.route('/user', methods=['POST'])
def create_user():
    """
    [POST] /api/product
    """
    u = User()
    data = {
        'id': request.get_json()['id'],
        'fname': request.get_json()['fname'],
        'location': request.get_json()['location']
    }
    u.from_dict(data)
    u.save()
    return jsonify(u.to_dict()), 201

@app.route('/user/<int:id>', methods=['PUT'])
def update_users(id):
    """
    [PUT] /api/product/<id>
    """
    u = User.query.get(id)
    data = {
        'fname': request.get_json()['fname'],
        'location': request.get_json()['location'],
    }
    u.from_dict(data)
    db.session.commit()
    return jsonify(u.to_dict())

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_product(id):
    """
    [DELETE] /api/product/<id>
    """
    u = User.query.get(id)
    db.session.delete(u)
    db.session.commit()
    return jsonify([u.to_dict() for u in User.query.all()])