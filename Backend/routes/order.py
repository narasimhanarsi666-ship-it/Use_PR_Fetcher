from flask import Blueprint, jsonify
order_bp = Blueprint("order", __name__)
ORDERS=[]

@order_bp.route("/create", methods=["POST"])
def create():
    o={"id":len(ORDERS)+1,"status":"CREATED"}
    ORDERS.append(o)
    return jsonify(o)

@order_bp.route("/")
def list():
    return jsonify(ORDERS)
