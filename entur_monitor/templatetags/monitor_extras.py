import dateutil.parser
from django import template

register = template.Library()


def time(value):
    try:
        return dateutil.parser.parse(value).strftime('%H:%M')
    except ValueError:
        return value


register.filter('time', time)


def color(line):
    """Show line color
    colors.json is generated from entur static data"""

    import json
    import os
    try:
        fp = open(os.path.dirname(__file__) + '/colors.json')
        colours = json.load(fp)
        if line in colours:
            return '#' + colours[line]
        else:
            return 'none'
    except FileNotFoundError:
        return 'none'


register.filter('color', color)
