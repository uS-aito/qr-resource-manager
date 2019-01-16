from django import template
register = template.Library()

@register.filter
def to_class_name(value):
    return value.__class__.__name__

@register.filter
def to_member_class_name(value):
    return value[0].__class__.__name__