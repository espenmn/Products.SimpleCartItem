## Script (Python) "getCurrencySymbol"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=returns the appropriate currency symbol based on the currency abbreviation set in prop sheet
##
from Products.CMFCore.utils import getToolByName

props = getToolByName(context, 'portal_properties')
currency = getattr(props.simplecartitem_properties, 'currency', None)

if currency:
    symbols = context.getAvailableCurrencyCodes()
    if symbols.has_key(currency):
        return symbols[currency]
    else:
        return currency
else:
    return ''