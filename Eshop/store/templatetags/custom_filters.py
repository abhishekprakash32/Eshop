from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    try:
        return value * arg
    except (TypeError, ValueError):
        return 0

@register.filter
def get_item(dictionary, key):
    """Retrieve an item from a dictionary by key."""
    return dictionary.get(str(key))
