from django import template

register = template.Library()

@register.simple_tag
def get_countries():
    return [
        {'name': 'Country 1'},
        {'name': 'Country 2'},
        {'name': 'Country 3'}
    ]


