from datetime import datetime
from django.utils import timezone


def check_time_token(token):
    now_date = timezone.now() + timezone.timedelta(hours=4)
    token_date = datetime.strptime(str(token),"%Y-%m-%d %H:%M:%S.%f%z")
    if now_date > token_date:
        return False
    else:
        return True 