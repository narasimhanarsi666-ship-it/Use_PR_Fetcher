from flask import Blueprint, jsonify
inventory_bp = Blueprint("inventory", __name__)
@inventory_bp.route("/status")
def status():
    return jsonify({"1":{"stock":10},"2":{"stock":0}})
