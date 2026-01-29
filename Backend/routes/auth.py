from flask import Blueprint, jsonify, request
auth_bp = Blueprint("auth", __name__)
USERS = {"admin": "admin123"}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json or {}
    if USERS.get(data.get("username")) != data.get("password"):
        return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({"token": "token-"+data["username"]})
