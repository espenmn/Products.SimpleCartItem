## Script (Python) "cart_size"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##title=Caclulates number of items in cart




cartList = context.REQUEST.SESSION['cartList']

total = 0
for item in cartList:
   total = total + item['quantity']

return total