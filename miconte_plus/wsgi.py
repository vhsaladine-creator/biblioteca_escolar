import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "miconte_plus.settings")
application = get_wsgi_application()
