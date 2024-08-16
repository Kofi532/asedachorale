from django import template

register = template.Library()

@register.filter(name='repeat')
def repeat(value, times):
    return value * times

@register.filter(name='index_to_voice')
def index_to_voice(index):
    voices = ["Soprano", "Alto", "Tenor", "Bass"]
    return voices[index] if index < len(voices) else ''


@register.filter
def range_filter(value):
    return range(value)

@register.filter
def add_one(value):
    return value + 1

@register.filter
def make_list(value):
    return range(int(value))