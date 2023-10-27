from django import template

register = template.Library()

@register.simple_tag
def calculate_total(count, price):
    return float(count)*float(price)