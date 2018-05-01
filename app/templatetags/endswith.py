from django import template

register = template.Library()


@register.filter('endswith')
def endswith(text, ends):
    return text.endswith(ends)
