## Script (Python) "postsale"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##title=Clears cart and redirects to thank you page

r= context.REQUEST
s = r.SESSION

s.delete('cartList')

sci = getattr(context.portal_properties, 'simplecartitem_properties', None)

url=context.portal_url()+ sci.getProperty('thankyou_page')
return r.RESPONSE.redirect(url)
