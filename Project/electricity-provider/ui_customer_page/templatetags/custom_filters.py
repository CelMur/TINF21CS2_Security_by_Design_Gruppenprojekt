import re
from django import template

register = template.Library()

@register.filter
def replace_none_with_null(value) -> str:
    return re.sub(r"&#x27;value&#x27;: None", "'value': null", value)