from flask import Flask
from routes.auth import auth_bp
from routes.user import user_bp
from routes.cart import cart_bp
from routes.checkout import checkout_bp
from routes.payment import payment_bp
from routes.order import order_bp
from routes.inventory import inventory_bp

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(cart_bp, url_prefix="/cart")
app.register_blueprint(checkout_bp, url_prefix="/checkout")
app.register_blueprint(payment_bp, url_prefix="/payment")
app.register_blueprint(order_bp, url_prefix="/order")
app.register_blueprint(inventory_bp, url_prefix="/inventory")

if __name__ == "__main__":
    app.run(debug=True)
