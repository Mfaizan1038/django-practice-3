from django import template
import datetime

register = template.Library() 



@register.simple_tag
def current_time():
    return datetime.datetime.now()



@register.simple_tag
def discounted_price(price, discount):
    """Returns price after discount"""
    return price - (price * discount / 100)
