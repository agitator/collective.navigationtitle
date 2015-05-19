from collective.navigationtitle import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform.directives import order_after
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class INavigationTitle(model.Schema):
    """Add tags to content
    """

    order_after(navigation_title='IBasic.title')
    order_after(navigation_title='IDublinCore.title')

    navigation_title = schema.TextLine(
        title=_(u"Navigation Title"),
        description=_(u"Short title that will be used in navigation."),
        required=False,
    )


@implementer(INavigationTitle)
class NavigationTitle(object):
    """
    """

    def __init__(self, context):
        self.context = context

#    @property
#    def tags(self):
#        return set(self.context.Subject())
#    @tags.setter
#    def tags(self, value):
#        if value is None:
#            value = ()
#        self.context.setSubject(tuple(value))
