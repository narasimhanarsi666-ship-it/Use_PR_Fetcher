from services.api import post
def login(u,p): return post('/auth/login',{'username':u,'password':p})
