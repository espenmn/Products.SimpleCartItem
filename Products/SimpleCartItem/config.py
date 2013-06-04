from Products.CMFCore.permissions import setDefaultRoles

PROJECTNAME = 'SimpleCartItem'

setDefaultRoles("SimpleCartItem: Add Simple Item", ('Manager', 'Owner', 'Contributor',))

ADD_PERMISSIONS = {
    "SimpleCartItem" : 'SimpleCartItem: Add Simple Item',
}
