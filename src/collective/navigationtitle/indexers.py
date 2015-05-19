from .interfaces import IShortTitleNavtreeStrategy
from plone.indexer import indexer


@indexer(IShortTitleNavtreeStrategy)
def short_title(obj):
    import ipdb; ipdb.set_trace()
    dx = IShortTitleNavtreeStrategy(obj, None)
    if dx is None:
        return None
    return dx.navigation_title
