#from datetime import datetime
#from Acquisition import aq_inner, aq_parent
#from zope.annotation.interfaces import IAnnotations
#from zope.component import getMultiAdapter, getUtility
#from plone.memoize.instance import memoize
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from Products.CMFCore.utils import getToolByName
#from Products.statusmessages.interfaces import IStatusMessage
#from currency.converter.interfaces import IRateAgainstBaseRate

class SimpleCartItemView(BrowserView):

    template = ViewPageTemplateFile('templates/simple_cart_item.pt')

    def __call__(self):
        return self.template()

