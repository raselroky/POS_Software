import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

# Assuming your Django settings module is named 'settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'business_software.settings')

# Uncomment the following lines if you have a virtual environment
# activate_this = os.path.join(os.path.dirname(__file__), 'path_to_your_virtualenv/bin/activate_this.py')
# exec(open(activate_this).read(), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()