from __future__ import absolute_import, unicode_literals
from config.celeryconfig import app
from celery.utils.log import get_task_logger
import webbrowser

logger = get_task_logger(__name__)


@app.task
def execute_cmd():
    url = "https://www.naver.com"

    logger.info(webbrowser.open(url))
