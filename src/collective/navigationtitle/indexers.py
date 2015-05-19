from .behaviors.navigation_title import INavigationTitle
from plone.indexer import indexer


@indexer(INavigationTitle)
def short_title(obj):
    import ipdb; ipdb.set_trace()
    dx = INavigationTitle(obj, None)
    if dx is None:
        return None
    return dx.navigation_title
