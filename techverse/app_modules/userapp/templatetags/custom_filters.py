from django import template

register = template.Library()

@register.filter
def split_half(value, part):
    midpoint = (len(value) + 1) // 2  # Left gets extra item if odd

    if part == "first":
        return value[:midpoint]
    elif part == "second":
        return value[midpoint:]
    return value
