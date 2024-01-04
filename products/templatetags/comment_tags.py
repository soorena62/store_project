from django import template

register = template.Library()  # Create library from this template filter


@register.filter
def only_active_comments(comments):
    return comments.filter(active=True)
