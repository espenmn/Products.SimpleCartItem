## Script (Python) "getAvailableCurrencyCodes"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=returns the currency codes available 
##

# if we're missing your country's currency code, customize this script and add it
return {
    'USD': u'$',
    'EUR': u'\u20ac',
    'GBP': u'\xa3',
    'CAD': u'CAD$',
    'NZD': u'NZD$',
    'JPY': u'\xa5',
    'CZK': u'K\u010d ',
    'NOK': u'kr ',
    'DKK': u'kr ',
    }