from services.paymentService import charge
from services.orderService import create_order
def checkout_flow(a): return create_order() if charge(a)['status']=='SUCCESS' else {'error':'fail'}
