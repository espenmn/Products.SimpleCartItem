## Script (Python) "setRef"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##title=Add items to cart

'''add url of last cart item to session so continue shopping works'''
request = container.REQUEST
RESPONSE =  request.RESPONSE

r = context.REQUEST
session = r.SESSION

# l is a list
hreflist=session.get("href")

hreflist = r.URL

# If you quit here, your changes to the list won't
# be saved. You need to save the session data by 
# reassigning it to the session.
session["href"]=hreflist