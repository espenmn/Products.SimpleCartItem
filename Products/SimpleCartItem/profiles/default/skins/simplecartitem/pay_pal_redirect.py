## Script (Python) "pay_pal_redirect"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##title=Formats cart items for payment gateway

'''This is the digester for the cart string.  Currently this digester formats a string to be sent to a Pay Pal gateway,
but could be modifed for other gateways'''

r= context.REQUEST
s = r.SESSION

# retrieve the cartList 
orderlist=s.get("cartList", [])


#NEED FUNCTION TO MAKE SURE CART IS UPDATED  NEEDS TO BE REFACTORED
#NEXT VERSION SHOULD USE CONTROLLER PAGE TEMPLATES
#the REQUEST pass the id of the item and the quantity

try:
    for key in r.form.keys():
        #again passing a list of id and option to the getItem function
        cart_item_id = key.split(',')
        existing_item = container.getItem(cart_item_id)
        if(existing_item is not None):
            existing_item['quantity'] = int(r.form[key])               
        

#handles invalid input for 'quantity'
except ValueError:
    pass
    


#END NEED UPDATE FUNCTION


#cart preamble
#Full of crufty stuff that should be using cpt
sci = getattr(context.portal_properties, 'simplecartitem_properties', None)
cart_commands = {"cmd"           : "_cart",
     "upload"        : "1",
     "business"      : sci.getProperty('account_id'),   
     "currency_code" : sci.getProperty('currency'), 
     "invoice"       : DateTime(),
     "no_shipping"   : "1",
     #thanks to Marcel Mare (WebToTheMax) for the following
     "cancel_return" : context.portal_url() +  sci.getProperty('cancel_page'), #this page needs to be set up in your site
     "return"        : context.portal_url() + '/postsale'  # runs a python script that clears the cart 
     }




# formats cart items 
l = 0

for item in orderlist:
    cart_item = item
    l+=1
    d ={'item_name_%d'  %l : cart_item['name'],
         'on0_%d' %l : '.',
         'os0_%d'  %l: cart_item['options'],
        'amount_%d'  %l : cart_item['price'],
        'quantity_%d'  %l : cart_item['quantity']
        }

    cart_commands.update(d)
    
    
#points to sandbox account, change as neededx
url = "https://www.paypal.com/us/cgi-bin/websc"

#assembles final url
param = []
for k, v in cart_commands.items():
  param.append("%s=%s" % (k, v))
param = "&".join(param)


return context.REQUEST.RESPONSE.redirect("%s?%s" % (url, param))
