from django import template
from datetime import datetime

register = template.Library()

@register.filter
def l2l_dt(value):
    try:
        if type(value) == str:
            value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
        return datetime.strftime(value, "%Y-%m-%d %H:%M:%S")
    except:
        return value
