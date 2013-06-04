from zope.interface import Interface
from zope import schema
from Products.SimpleCartItem import SimpleCartItemMessageFactory as _

class ISimpleCartItem(Interface):
    """Interface for SimpleCartItem content type.
    """

    price = schema.Float(
        title=_(u"Price"),
        description=_(u'Price for your item -- do NOT include currency symbols!'),
        required=True,
    )

    description = schema.Text(
        title=_(u"Basic Description"),
        description=_(u"Short description of the item; it will show up in listing views."),
        required=False,
    )

    short_description = schema.Text(
        title=_(u"Extended Description"),
        description=_(u"Detailed description of the item."),
        required=True,
    )

    options_description = schema.TextLine(
        title=_(u"Options Label"),
        description=_(u'For instance, Size or Colors.'),
        required=False,
    )

    instock = schema.Bool(
        title=_(u"Is this item in stock?"),
        description=_(u'If it is not in stock, shoppers can see all the information about it, but cannot actually add it to their cart.'),
        required=False,
        default=True,
    )
