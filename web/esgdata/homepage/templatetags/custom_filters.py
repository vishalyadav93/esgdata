# yourapp/templatetags/custom_filters.py
from django import template
import os

register = template.Library()  # Registering the library for custom tags and filters

@register.filter(name='basename')
def basename(value):
    """
    Custom filter to get the base file name from a full path.
    """
    return os.path.basename(value)
