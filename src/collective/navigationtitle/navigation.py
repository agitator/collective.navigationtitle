# -*- coding: utf-8 -*-
from plone.app.portlets.portlets.navigation import NavtreeStrategy
from zope.interface import implementer
from zope.component import adapter
from plone.app.layout.navigation.interfaces import INavtreeStrategy
from plone.app.portlets.portlets.navigation import INavigationPortlet
from Products.CMFCore.interfaces import IContentish


class BrainWrapper(object):

    def __init__(self, brain):
        self.brain = brain

    def __getattr__(self, name):
        if name == 'Title':
            return self.brain.short_title
        else:
            return getattr(self.brain, name)


@implementer(INavtreeStrategy)
@adapter(IContentish, INavigationPortlet)
class ShortTitleNavtreeStrategy(NavtreeStrategy):

    def decoratorFactory(self, node):
        node['item'] = BrainWrapper(node['item'])
        return node
