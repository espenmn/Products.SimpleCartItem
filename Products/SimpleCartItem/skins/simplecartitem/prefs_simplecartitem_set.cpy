## Controller Script (Python) "prefs_navigation_set"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=account_id='youremail@yourpaymentgateway.com', currency='USD', cancel_page='/', thankyou_page='/', gateway_script='pay_pal_redirect',RESPONSE=None
##title=Set SimpleCartItem Prefs
##

from Products.CMFCore.utils import getToolByName
from Products.SimpleCartItem.utils import sci_addPortalMessage

REQUEST=context.REQUEST
portal_properties=getToolByName(context, 'portal_properties')

portal_properties.simplecartitem_properties.manage_changeProperties(
                        account_id=account_id,
                        currency=currency,
                        cancel_page=cancel_page,
                        thankyou_page=thankyou_page,
						gateway_script=gateway_script
                        )

msg = sci_addPortalMessage('SimpleCartItem settings updated.', context)
return state.set(portal_status_message=msg)
