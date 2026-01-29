from flask import Blueprint, jsonify, request
from utils.retry import retry_payment
payment_bp = Blueprint("payment", __name__)

@payment_bp.route("/charge", methods=["POST"])
def charge():
    amt=request.json.get("amount",0)
    if amt<=0:
        return jsonify({"status":"FAILED"}),400
    return jsonify({"status":"SUCCESS" if retry_payment() else "FAILED"})
