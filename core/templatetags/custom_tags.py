from django import template
from django.urls import resolve

register = template.Library()


@register.simple_tag
def is_active(request, url_name):
    """
    Usage: {% is_active request "url_name" %}
    Returns 'active' if the current request's path matches the given URL name.
    """
    current_url_name = resolve(request.path).url_name
    return 'active' if current_url_name == url_name else ''
