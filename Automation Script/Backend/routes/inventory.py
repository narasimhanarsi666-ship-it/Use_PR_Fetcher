def test_inventory_available():
    inventory={1:{"stock":10}}
    return inventory[1]["stock"]>0

def test_inventory_out_of_stock():
    inventory={2:{"stock":0}}
    return inventory[2]["stock"]==0
