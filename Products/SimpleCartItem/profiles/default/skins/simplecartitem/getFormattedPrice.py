## Script (Python) "getFormattedPrice"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=price
##title=returns formatted price to two decimal places prefaced by currency symbol
##

if price:
    return '%s%.2f' % (context.getCurrencySymbol(), price)
else:
    return ''