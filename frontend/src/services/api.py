import requests
BASE_URL='http://localhost:5000'
def get(p): return requests.get(BASE_URL+p).json()
def post(p,b=None): return requests.post(BASE_URL+p,json=b).json()
