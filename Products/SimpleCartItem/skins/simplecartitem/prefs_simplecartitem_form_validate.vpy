from Products.CMFCore.utils import getToolByName
_ = context.translate
    
request = context.REQUEST

required = ('account_id', 'currency','cancel_page','thankyou_page','gateway_script')


for k in required:
    v = request.form.get(k, '').strip()
    if not v:
        state.setError(k, _('Input is required but not given.', domain='simplecartitem'))


cancel_page = request.form.get('cancel_page', None)
if cancel_page and cancel_page != '/':
    purl = getToolByName(context, 'portal_url')
    cancel_pagePath = purl.getPortalPath() + cancel_page
    try:
        cancel_pageObject = purl.getPortalObject().restrictedTraverse(cancel_pagePath)
    except KeyError:
        cancel_pageObject = None  
    if cancel_pageObject is None:
        state.setError('cancel_page', _(msgid='cancelpage_not_found', default='Could not find ${cancel_page}', mapping={'cancel_page':'cancel_page'}, domain='simplecartitem'))


thankyou_page = request.form.get('thankyou_page', None)
if thankyou_page and thankyou_page != '/':
    purl = getToolByName(context, 'portal_url')
    thankyou_pagePath = purl.getPortalPath() + thankyou_page
    try:
        thankyou_pageObject = purl.getPortalObject().restrictedTraverse(thankyou_pagePath)
    except KeyError:
        thankyou_pageObject = None
    if thankyou_pageObject is None:
        state.setError('thankyou_page', _(msgid='thankyoupage_not_found', default='Could not find ${thankyou_page}', mapping={'thankyou_page':'thankyou_page'}, domain='simplecartitem'))

if state.getErrors():
    return state.set(status='failure',
        portal_status_message=_('Please correct the indicated errors.', domain='simplecartitem'))
else:
    return state

