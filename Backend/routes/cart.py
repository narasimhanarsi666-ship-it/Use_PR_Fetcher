import Blueprint
from flask import Blueprint, jsonify, request
cart_bp = Blueprint("cart", __name__)
CART=[]

@cart_bp.route("/add", methods=["POST"])
def add():
    item=request.json
    if not item or "id" not in item:
        return jsonify({"error":"invalid"}),400
    CART.append(item)
    return jsonify(CART)

@cart_bp.route("/")
def get():
    return jsonify(CART)
