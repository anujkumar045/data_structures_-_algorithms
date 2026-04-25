cart={}
def add(cart,brand,price,qty):
    if brand in cart:
        cart[brand][qty]+=qty
    else:
        cart[brand]={ 'price': price, 'qty': qty}
    return cart

def remove(cart):
    if brand in cart:
        cart.pop()
    else:
        pass
    return

def view(cart,brand,price,qty):
    if brand not in cart:
        print("Empty cart")
    else:
        for brand in cart:
            'brand'=cart.brand()
            print('brand')


brand=input("Enter name")
price=int(input("Enter price"))
qty=int(input("Enter qty"))
res=add(cart,brand,price,qty)
print(res)

