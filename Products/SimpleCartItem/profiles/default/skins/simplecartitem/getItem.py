## Script (Python) "getItem"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cart_item
##title=Gets cart_item from cartList based on id and options

'''Script provides an accessor for items in orderlist'''
r = container.REQUEST
session = r.SESSION

#orderlist contains all items
orderlist=session.get("cartList", [])

try:
    for existing_item in orderlist:
        if(existing_item['id'] == cart_item[0] and existing_item['options'] == cart_item[1]):
            return existing_item
except KeyError:
    return None

