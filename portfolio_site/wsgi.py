"""
WSGI config for portfolio_site project.

This file is used when you deploy your site to a host.

Your browser can't talk directly to Django. A translation must be made. This is what WSGI (pronounced /whiskey/) does.
WSGI stands for 'Web Server Gateway Interface' and is a standard that allows the webserver of your host to communicate with your Django application.

Remember: Wagtail itself is build on top Django, your Wagtail project IS a Django project! Anything that applies to Django applies to Wagtail too.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings.production")

application = get_wsgi_application()
