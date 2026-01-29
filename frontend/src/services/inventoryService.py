from services.api import get
def get_inventory(): return get('/inventory/status')
