try:
    from Zope2.App import zcml
except ImportError:
    from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup_product():

    fiveconfigure.debug_mode = True
    import Products.SimpleCartItem
    zcml.load_config('configure.zcml', Products.SimpleCartItem)
    import Products.DataGridField
    zcml.load_config('configure.zcml', Products.DataGridField)

    fiveconfigure.debug_mode = False

    ztc.installProduct('SimpleCartItem')
    ztc.installProduct('DataGridField')

#ztc.installProduct('SimpleCartItem')
setup_product()
ptc.setupPloneSite(products=['SimpleCartItem', 'DataGridField'])
#ptc.setupPloneSite(products=['SimpleCartItem',])

class TestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package. If
    necessary, we can put common utility or setup code in here. This
    applies to unit test cases.
    """


class FunctionalTestCase(ptc.FunctionalTestCase):
    """We use this class for functional integration tests that use
    doctest syntax. Again, we can put basic common utility or setup
    code in here.
    """

#    def afterSetUp(self):
#        roles = ('Member', 'Contributor')
#        self.portal.portal_membership.addMember('contributor',
#                                                'secret',
#                                                roles, [])
