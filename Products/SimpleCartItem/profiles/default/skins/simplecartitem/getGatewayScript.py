## Script (Python) "getGatewayScript"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##title=Add items to cart

'''add item to cart, creates cart if it does not exist'''

r = container.REQUEST
session = r.SESSION


sci = getattr(context.portal_properties, 'simplecartitem_properties', None)
gateway_script = sci.getProperty('gateway_script')

return gateway_script + ":method"
