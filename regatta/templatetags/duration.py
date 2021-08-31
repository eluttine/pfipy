from django import template
from datetime import timedelta


register = template.Library()


@register.filter
def duration(seconds):
    return str(timedelta(seconds=seconds))
