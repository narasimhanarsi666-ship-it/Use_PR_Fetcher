from flask import Blueprint, jsonify
checkout_bp = Blueprint("checkout", __name__)

@checkout_bp.route("/start", methods=["POST"])
def start():
    return jsonify({"status":"CHECKOUT_STARTED"})
