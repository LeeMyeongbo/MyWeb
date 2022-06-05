call activate
call celery -A config worker --loglevel=info --pool=solo
