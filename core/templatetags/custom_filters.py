from django import template

register = template.Library()
@register.filter
def account_for_pagination(value, page):
    value, page = int(value), int(page)
    counter_value = value + ((page - 1) * 50)
    return counter_value