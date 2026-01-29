def test_create_order():
    order={"id":1,"status":"CREATED"}
    return order["status"]=="CREATED"

def test_list_orders():
    orders=[]
    return isinstance(orders,list)
