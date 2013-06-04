from zope.interface import implements

#try:
#  from Products.LinguaPlone.public import *
#except ImportError:
#  # No multilingual support
#  from Products.Archetypes.public import *

from Products.Archetypes.public import (
    BaseSchema,
    Schema,
    registerType,
    BooleanField,
    FloatField,
    ImageField,
    StringField,
    TextField,
    BooleanWidget,
    DecimalWidget,
    ImageWidget,
    RichWidget,
    StringWidget,
    TextAreaWidget,
)
from Products.ATContentTypes.content.base import ATCTContent
from Products.Archetypes.Marshall import RFC822Marshaller
#from Products.CMFCore import permissions

from Products.DataGridField import (
    Column,
    DataGridField,
    DataGridWidget
)
from Products.SimpleCartItem import PROJECTNAME
from Products.SimpleCartItem.interfaces import ISimpleCartItem

schema = BaseSchema.copy() +  Schema((

    FloatField(
        name = 'price',
        required = False,
        widget = DecimalWidget(
            label='Price',
            description='Price for your item -- do NOT include currency symbols!',
            label_msgid='label_price',
            description_msgid='help_price',
            i18n_domain='simplecartitem',
        ),
        validator='isDecimal',
    ),

    TextField(
        name = 'description',
        searchable = True,
        widget = TextAreaWidget(
            label='Basic Description',
            description='Short description of the item; it will show up in listing views.',
            allow_file_upload = False,
            label_msgid='label_description',
            description_msgid='help_description',
            i18n_domain='simplecartitem',
        ),
        isMetadata=True,
        accessor='Description', 
        default_output_type='text/plain',
        allowable_content_types=('text/plain',),
    ),

    TextField(
        name = 'short_description',
        searchable = True,
        widget=RichWidget(
            label='Extended Description',
            description='Detailed description of the item.',
            allow_file_upload = False,
            label_msgid='label_short_description',
            description_msgid='help_short_description',
            i18n_domain='simplecartitem',
        ),
        required=False,
        default_output_type='text/html',
        allowable_content_types=(
            'text/html',
            'text/plain',
            'text/structured',
        ),
    ),

    StringField(
        name='options_description',
        searchable=True,
        widget= StringWidget(
            label='Options Label',
            description="""For instance, Size or Colors.""",
            label_msgid='label_options_description',
            description_msgid='help_options_description',
            i18n_domain='simplecartitem',
        ),
        required=False,
        default_output_type='text/html',
        allowable_content_types=('text/plain'),
    ),

    DataGridField(
        name='options',
        searchable = True,
        columns=("option", "price_adjustment"),
        allow_empty_rows = False,
        widget = DataGridWidget(
            label='Options',
            auto_insert = True,
            description="""For instance, "Small", "Medium", and "Large", or "Brown", "Black", and "Red".  You may add as many or few options as you like.""",
            label_msgid='label_options',
            description_msgid='help_options',
            i18n_domain='simplecartitem',
            columns={
                'option' : Column("Option", label_msgid='label_column_option'),
                'price_adjustment' : Column("Price Adjustment", label_msgid='label_column_priceadjustment'),
            },
        ),
    ),

    ImageField(
        name='image',
        default_output_type='image/jpeg',
        allowable_content_types=('image/*',),
        widget=ImageWidget(
            label='Image',
            description='Optionally upload a picture of the item',
            macro_view='flex_image',
            label_msgid='label_image',
            description_msgid='help_image',
            i18n_domain='simplecartitem',
        ),
    ),

    BooleanField(
        name='instock',
        index='FieldIndex:schema',
        default=True,
        widget=BooleanWidget(
            label='Is this item in stock?',
            description="""If it is not in stock, shoppers can see all the information about it, but cannot actually add it to their cart.""",
            label_msgid='label_instock',
            description_msgid='help_instock',
            i18n_domain='simplecartitem',
        ),
    ),

    ),
    marshall=RFC822Marshaller(),
    )


class SimpleCartItem(ATCTContent):
    """Simple Cart Item
    """

    implements(ISimpleCartItem)
#    meta_type =  'SimpleCartItem'
#    portal_type = archetype_name = 'Cart Item'
#    immediate_view = 'simplecartitem_view'
#    default_view   = 'simplecartitem_view'
#    content_icon   = "cart1_icon.gif"
    schema = schema

    # Make sure we get title-to-id generation when an object is created
    _at_rename_after_creation = True

registerType(SimpleCartItem, PROJECTNAME)
