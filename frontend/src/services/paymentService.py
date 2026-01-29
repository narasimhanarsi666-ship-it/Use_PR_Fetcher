from services.api import post
def charge(a): return post('/payment/charge',{'amount':a})
