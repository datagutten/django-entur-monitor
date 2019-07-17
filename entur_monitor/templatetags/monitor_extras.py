import dateutil.parser
from django import template

register = template.Library()


def time(value):
    return dateutil.parser.parse(value).strftime('%H:%M')


register.filter('time', time)
