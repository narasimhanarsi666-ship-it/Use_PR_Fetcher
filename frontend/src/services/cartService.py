from services.api import post,get
def add_item(i): return post('/cart/add',i)
def get_cart(): return get('/cart/')
