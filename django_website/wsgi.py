# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
import dotenv
from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application

## assuming your django settings file is at '/home/amadejpapez/mysite/mysite/settings.py'
## and your manage.py is is at '/home/amadejpapez/mysite/manage.py'
path = "/home/amadejpapez/website"
if path not in sys.path:
    sys.path.append(path)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_file = os.path.join(BASE_DIR, ".env")

if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SECRET_KEY = os.getenv('SECRET_KEY')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_website.settings')
if settings.DEBUG:
    application = StaticFilesHandler(get_wsgi_application())
else:
    application = get_wsgi_application()