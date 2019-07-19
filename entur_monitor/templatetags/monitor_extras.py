import dateutil.parser
from django import template

register = template.Library()


def time(value):
    try:
        return dateutil.parser.parse(value).strftime('%H:%M')
    except ValueError:
        return value


register.filter('time', time)
