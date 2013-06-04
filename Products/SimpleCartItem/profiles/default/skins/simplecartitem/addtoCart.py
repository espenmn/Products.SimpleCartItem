## Script (Python) "addtoCart"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##title=Add items to cart

'''add item to cart, creates cart if it does not exist'''

r = container.REQUEST
session = r.SESSION

# retrieve the cartList if it exists
cartList=session.get("cartList", [])

#look up the dictionary
#options are stored as a tuple of dictionaries, convert to list so we can do something with it
options = list(context.getOptions())
options_dict = {}

#difficult to get reliable dictionaries passed directly from the form, so instead look up the dictionary based on the option key.
for dict in options:
    if dict['option'] == r.form['options']:
       options_dict = dict
        
#set item options
itemoptions = options_dict. get('option', '')

#adjust price if part of options
try:
    price = context.getPrice() + float(options_dict.get('price_adjustment', 0.0))
except ValueError:
    price = context.getPrice()

#storing the cart object in the session directly was not an option (produced storage error
#in its place is a representation of the necessary values that are to be sent to the digester

#create cart item to store in session
cart_item = {'id':context.getId(), 'price': price, 'name':context.Title(), 'options':itemoptions,'quantity': 1}

#Use list comprehension to build a list of tuples containing the id and options. This allows for
#comparison between the incoming cart_item and those already in the cartList session object.
#Comparing cart_item objects directly does not works since the value of the object differs depending on the options selected and the quantity of items in the cart.

existing_item_ids = [(existing_item['id'],existing_item['options']) for existing_item in cartList]

#See if incoming cart_item exists by search for the index of the tuple 

try:
    index = existing_item_ids.index((cart_item['id'],cart_item['options']))
    cartList[index]['quantity'] = cartList[index]['quantity'] + 1    
    #handle the exception is it does not. Since there is not an existing item, it can be added to the list
except ValueError:  
    cartList.append(cart_item)
  
# If you quit here, your changes to the list won't
# be saved. You need to save the session data by 
# reassigning it to the session.
#the reason is that the session object is a list of tuples

session["cartList"]=cartList

r.RESPONSE.redirect('cart')
