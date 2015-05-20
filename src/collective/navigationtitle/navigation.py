# -*- coding: utf-8 -*-
from .interfaces import IShortTitleNavtreeStrategy
from plone.app.layout.navigation.navtree import NavtreeStrategyBase
from zope.interface import implementer
from zope.component import adapter
from plone.app.layout.navigation.interfaces import INavtreeStrategy
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.portlets.portlets.navigation import INavigationPortlet
from Products.CMFCore.interfaces import IContentish

from OFS.interfaces import IItem


class BrainWrapper(object):

    def __init__(self, brain):
        self.brain = brain

#    def __getattr__(self, name):
#        import ipdb; ipdb.set_trace()
#        if name == 'Title':
#            return self.brain.short_title
#        else:
#            return getattr(self, brain)


@implementer(INavtreeStrategy)
@adapter(IContentish, INavigationPortlet)
class ShortTitleNavtreeStrategy(NavtreeStrategyBase):

    def decoratorFactory(self, node):
        import ipdb; ipdb.set_trace()
#        node['item'] = BrainWrapper(node['item'])
#        return node
