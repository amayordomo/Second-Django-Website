from django import template

register = template.Library()

@register.filter(name='custom_filter')
def my_filter(value):
    return value + " This is a string from a custom filter"
