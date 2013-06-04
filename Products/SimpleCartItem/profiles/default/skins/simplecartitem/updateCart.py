## Script (Python) "updateCart"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##title=Updates items in the cart

'''updates the quantity for a particular item'''
from Products.SimpleCartItem.utils import sci_addPortalMessage

r = container.REQUEST
session = r.SESSION
_ = context.translate
#the REQUEST pass the id of the item and the quantity

try:
    for key in r.form.keys():
        #again passing a list of id and option to the getItem function
        cart_item_id = key.split(',')
        existing_item = container.getItem(cart_item_id)
        if(existing_item is not None):
            existing_item['quantity'] = int(r.form[key])               
    msg = sci_addPortalMessage('Cart updated.', context)
        
#handles invalid input for 'quantity'
except ValueError:
    msg = sci_addPortalMessage('Please enter a number', context)

return context.REQUEST.RESPONSE.redirect('%s/cart?%s' % (context.absolute_url(), msg))

