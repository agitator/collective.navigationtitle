# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from collective.navigationtitle import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class INavigationTitleLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IShortTitleNavtreeStrategy(Interface):
    """Marker Interface for the NavigationTitle"""