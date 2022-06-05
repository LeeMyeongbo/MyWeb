import os
import sys
import site

activate_this = 'C:/Users/myeon/MB_workspace/myweb_git/venv/Scripts/activate_this.py'

exec(open(activate_this).read(), dict(__file__=activate_this))

# 가상환경의 패키지 추가
site.addsitedir('C:/Users/myeon/MB_workspace/myweb_git/venv/Scripts/Lib/site-packages')

# PYTHONPATH에 application directory 추가
path = os.path.abspath(__file__ + '/../..')
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
