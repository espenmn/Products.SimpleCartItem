## Script (Python) "deleteItem"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cart_item=[]
##title=Delete items from the cart
##
from Products.SimpleCartItem.utils import sci_addPortalMessage

r = container.REQUEST
session = r.SESSION

cartList=session.get("cartList", [])
cart_ids = r.get('cart_item', [])

if cart_ids:
    for cart_item_id in cart_ids:
        cart_item_id = cart_item_id.split(',')
        cartList.remove(container.getItem(cart_item_id))
    msg = sci_addPortalMessage('Cart updated.', context)
else:
    msg = sci_addPortalMessage('No items selected.', context)

session["cartList"]=cartList
return context.REQUEST.RESPONSE.redirect('%s/cart?%s' % (context.absolute_url(), msg))
