from collective.navigationtitle import _
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class INavigationTitle(model.Schema):
    """Add tags to content
    """

#    directives.fieldset(
#        'categorization',
#        label=_(u'Default'),
#        fields=('navigation_title',),
#    )

    navigation_title = schema.TextLine(
        title=_(u"Tags"),
        description=_(u"Applicable tags"),
        required=False,
    )


@implementer(INavigationTitle)
class NavigationTitle(object):
    """
    """

    def __init__(self, context):
        self.context = context
