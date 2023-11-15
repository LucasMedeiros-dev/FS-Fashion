from django import template
from django.urls import resolve

register = template.Library()


@register.simple_tag
def active_app(request, app_name):
    current_url = request.path
    resolved_view = resolve(current_url)

    if resolved_view.app_name == app_name:
        return 'active'
    return ''


@register.simple_tag
def open_app(request, app_name):
    current_url = request.path
    resolved_view = resolve(current_url)

    if resolved_view.app_name == app_name:
        return 'menu-open'
    return ''


@register.simple_tag
def active_view(request, app_name, view_name):
    current_url = request.path
    resolved_view = resolve(current_url)

    if resolved_view.app_name == app_name and resolved_view.url_name == view_name:
        return 'active'
    return ''
