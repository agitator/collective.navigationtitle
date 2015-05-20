# -*- coding: utf-8 -*-
from .interfaces import IShortTitleNavtreeStrategy
from plone.app.layout.navigation.navtree import NavtreeStrategyBase
from zope.interface import implementer
from plone.app.layout.navigation.interfaces import INavtreeStrategy

class BrainWrapper(object):

    def __init__(self, brain):
        self.brain = brain

    def __getattr__(self, name):
        import ipdb; ipdb.set_trace()
        if name == 'Title':
            return self.brain.short_title
        else:
            return getattr(self, brain)


@implementer(INavtreeStrategy)
class ShortTitleNavtreeStrategy(NavtreeStrategyBase):

    def decoratorFactory(self, node):
        import ipdb; ipdb.set_trace()
        node['item'] = BrainWrapper(node['item'])
        return node
