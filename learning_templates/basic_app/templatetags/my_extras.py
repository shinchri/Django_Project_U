# for custom template filter

from django import template

# one way of doing it, can use decorators
register = template.Library()

# create custom filter
@register.filter(name='cut')  # uses decorators instead
def cut(value, arg):
    """
    this cuts out all values of 'arg' from the string!
    """

    return value.replace(arg,'')

#first parameter: what to call it
#second value : what function
#register.filter('cut', cut)

