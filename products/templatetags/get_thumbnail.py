__author__ = 'NESCODE'

from django import template

register = template.Library()

from ..models import Product, THUMB_CHOICES

@register.filter
def get_thumbnail(obj, arg):
    """
    obj == Product instance

    """
    arg = arg.lower()
    if not isinstance(obj, Product):
        return None

    # Compare with keys instead of relying on a dict conversion that might fail on some Python versions
    valid_types = [choice[0] for choice in THUMB_CHOICES]
    if arg not in valid_types:
        return None
        
    try:
        thumb = obj.thumbnail_set.filter(type=arg).first()
        if thumb and thumb.media:
            return thumb.media.url
    except Exception:
        pass
    return None
