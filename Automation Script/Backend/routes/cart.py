def test_add_valid_item():
    item={"id":1,"price":10}
    return "id" in item and "price" in item

def test_add_invalid_item():
    item={}
    return "id" not in item
