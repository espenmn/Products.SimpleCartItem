try:
    import unittest2 as unittest
except ImportError:
    import unittest
from Products.CMFCore.utils import getToolByName
from Products.SimpleCartItem.tests.base import TestCase

class TestSetup(TestCase):

    def afterSetUp(self):
        self.catalog = getToolByName(self.portal, 'portal_catalog')
        self.types = getToolByName(self.portal, 'portal_types')
        self.wftool = getToolByName(self.portal, 'portal_workflow')
        self.content_types = [
            'SimpleCartItem',
        ]
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.skins      = getToolByName(self.portal, 'portal_skins')
        self.properties = getToolByName(self.portal, 'portal_properties')
        self.site_properties = getattr(self.properties, 'site_properties')
        self.navtree_properties = getattr(self.properties, 'navtree_properties')
        self.controlpanel = getToolByName(self.portal, 'portal_controlpanel')

    def test_is_SimpleCartItem_installed(self):
        self.failUnless(self.installer.isProductInstalled('SimpleCartItem'))

    def test_is_DataGridField_installed(self):
        self.failUnless(self.installer.isProductInstalled('DataGridField'))

#    def testSkinLayersInstalled(self):
#        self.failUnless('simplecartitem' in self.skins.objectIds())

    ## Content Types
    def test_contents_installed(self):
        for type in self.content_types:
            self.failUnless(type in self.types.objectIds())

    def test_use_folder_tabs(self):
        if self.site_properties.getProperty('use_folder_tabs') is not None:
            self.failUnless('SimpleCartItem' not in self.site_properties.getProperty('use_folder_tabs'))

    def test_typesLinkToFolderContentsInFC(self):
        self.failUnless('SimpleCartItem' not in self.site_properties.getProperty('typesLinkToFolderContentsInFC'))

    def test_simple_cart_item_content_type(self):
        item = self.types.getTypeInfo('SimpleCartItem')
        self.assertEquals('Simple Cart Item', item.title)
        self.assertEquals('Simple Cart Item', item.description)
        self.assertEquals('SimpleCartItem', item.content_meta_type)
        self.assertEquals('addSimpleCartItem', item.factory)
        self.assertEquals('view', item.immediate_view)
        self.assertEquals(True, item.global_allow)
        self.assertEquals(False, item.filter_content_types)
        self.assertEquals((), item.allowed_content_types)
        self.assertEquals('view', item.default_view)
        self.assertEquals(('view',), item.view_methods)
        aliases = {'edit': 'atct_edit', 'sharing': '@@sharing', '(Default)': '(dynamic view)', 'view': '(selected layout)'}
        self.assertEquals(aliases, item.getMethodAliases())
        actions = [
            (action.title, action.id, action.getActionExpression(), action.visible, action.permissions) for action in item.listActions()
        ]
        self.assertEquals(
            [
                ('View', 'view', 'string:${object_url}', True, (u'View',)),
                ('Edit', 'edit', 'string:${object_url}/edit', True, (u'Modify portal content',))
            ],
            [
                (action.title, action.id, action.getActionExpression(), action.visible, action.permissions) for action in item.listActions()
            ]
        )


#    def test_simplecartitem_properties(self):
#        simplecartitem_properties = getattr(self.properties, 'simplecartitem_properties')
#        self.assertEquals('youremail@yourpaymentgateway.com', simplecartitem_properties.getProperty('account_id'))
#        self.assertEquals('USD', simplecartitem_properties.getProperty('currency'))
#        self.assertEquals('/', simplecartitem_properties.getProperty('cancel_page'))
#        self.assertEquals('/', simplecartitem_properties.getProperty('thankyou_page'))

#    ## navtree_properties
#    def test_not_in_navtree(self):
#        self.failUnless('SimpleCartItem' in self.navtree_properties.getProperty('metaTypesNotToList'))

#    ## controlpanel.xml
#    def test_configlet(self):
#        act = [action for action in self.controlpanel.listActions() if action.id == 'simplecartitem_config'][0]
#        self.assertEquals(u'Simple Cart Item Config', act.title)
#        self.assertEquals("SimpleCartItem", act.appId)
#        try:
#            self.assertEquals("string:${portal_url}/cart1_icon.gif", act.icon_expr.text)
#        except AttributeError:
#            pass
#        self.assertEquals("string:${portal_url}/prefs_simplecartitem_form", act.action.text)

    # Workflow
    def test_workflow(self):
        self.assertEquals(('simple_publication_workflow',), self.wftool.getChainForPortalType('SimpleCartItem'))

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
