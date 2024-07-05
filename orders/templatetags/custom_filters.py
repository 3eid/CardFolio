from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def flatatt(attrs):
    return format_html(''.join(f' {key}="{value}"' for key, value in attrs.items()))