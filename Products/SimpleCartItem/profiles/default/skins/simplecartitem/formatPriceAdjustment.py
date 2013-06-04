## Script (Python) "formatPriceAdjustment"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=price_adjustment=None
##title=Formats the price adjustment number]

adjustment_text = ''
adjustment = 0

try:
    adjustment = float(price_adjustment)
    adjustment_text = "%+.2f"  % (adjustment)

except ValueError:
    adjustment_text = ''    

return adjustment_text
