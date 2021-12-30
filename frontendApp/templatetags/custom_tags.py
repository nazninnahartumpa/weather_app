from django import template
from datetime import datetime, timedelta
import pytz
register = template.Library()

@register.filter(name='convert_only_dateYear')
def convert_date(given_time):
    d = str(given_time)
    final_result = datetime.fromtimestamp(int(d)).strftime('%b %d, %Y')
    return final_result


@register.filter(name='convert_only_time')
def convert_time(given_time):
    d = str(given_time)
    timestamp = datetime.fromtimestamp(int(d))
    final_result = timestamp.strftime("%I:%M %p")
    return final_result



@register.filter
def to_and(value):
    return value.replace("en/", "")