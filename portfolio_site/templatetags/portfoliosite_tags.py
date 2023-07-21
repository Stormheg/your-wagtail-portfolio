from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def is_current_page(context, page_being_checked):
    """Custom template tag. It is used to check if the `page_being_checked` is the page we are current on.

    This is used to show the nightlight the current in the navigation."""

    # Get the current page we are on
    current_page = context.get("page")

    # If the current page id matches the page id we are checking, it must the active page
    if current_page.id == page_being_checked.id:
        return True

    # Not the active page
    return False
