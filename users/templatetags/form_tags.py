from django import template
from django.forms import BaseForm, BoundField

register = template.Library()

@register.filter
def add_class(field, css_class):
    if isinstance(field, BoundField):
        widget = field.field.widget
        if 'class' in widget.attrs:
            widget.attrs['class'] += ' ' + css_class
        else:
            widget.attrs['class'] = css_class
        return field
    elif isinstance(field, BaseForm):
        for bound_field in field:
            widget = bound_field.field.widget
            if 'class' in widget.attrs:
                widget.attrs['class'] += ' ' + css_class
            else:
                widget.attrs['class'] = css_class
        return field
    return field
