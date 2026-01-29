from services.api import post,get
def create_order(): return post('/order/create')
def get_orders(): return get('/order/')
