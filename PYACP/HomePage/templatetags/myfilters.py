from django import template
import re
register = template.Library()


@register.filter
def add_b(key):
    key = str(key)
    return key+'%'

