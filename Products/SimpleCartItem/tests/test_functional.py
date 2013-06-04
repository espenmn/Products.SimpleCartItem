import os
import unittest
import doctest
from Testing import ZopeTestCase as ztc
from Products.SimpleCartItem.tests import base
from Products.CMFCore.utils import getToolByName

class TestSetup(base.FunctionalTestCase):

    def afterSetUp( self ):
        """After SetUp"""
        self.setRoles(('Manager',))
        ## Set up sessioning objects
        ztc.utils.setupCoreSessions(self.app)
#        portal = self.portal

def test_suite():
    return unittest.TestSuite([

        ztc.FunctionalDocFileSuite(
            'tests/functional/content_type_functional.txt',
            package='Products.SimpleCartItem',
            test_class=TestSetup,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),

            ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
