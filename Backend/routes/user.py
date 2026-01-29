from flask import Blueprint, jsonify
user_bp = Blueprint("user", __name__)

@user_bp.route("/me")
def me():
    return jsonify({"id":1,"name":"Admin","email":"admin@example.com"})
