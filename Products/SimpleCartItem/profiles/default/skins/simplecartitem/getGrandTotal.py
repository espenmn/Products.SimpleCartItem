## Script (Python) "getGrandTotal"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
'''Script provides a grand total for all items in the cart'''
r = container.REQUEST
session = r.SESSION
#orderlist contains all items
orderlist=session.get("cartList", [])

total = 0

try:
    for cart_item in orderlist:
        total = total + (cart_item['quantity'] * float(cart_item['price']))

except KeyError:
    return None

#if total > 679:
#    total = total*75/100

#total = total+55

return int(total)
