# -*- coding: utf-8 -*-
from .interfaces import IShortTitleNavtreeStrategy
from plone.app.layout.navigation.navtree import NavtreeStrategyBase
from zope.interface import implementer


class BrainWrapper(object):

    def __init__(self, brain):
        self.brain = brain

    def __getattr__(self, name):
        if name == 'Title':
            return self.brain.short_title
        else:
            return getattr(self, brain)


@implementer(IShortTitleNavtreeStrategy)
class ShortTitleNavtreeStrategy(NavtreeStrategyBase):

    def decoratorFactory(self, node):
        node['item'] = BrainWrapper(node['item'])
        return node
