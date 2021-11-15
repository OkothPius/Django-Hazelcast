from django import template
register = template.Library()

@register.filter(name='get_value')
def get_value(dict, key):
    return dict[key]

register.filter('get_value', get_value)


# @register.simple_tag
# def label(value, key):
#     return value[key]
