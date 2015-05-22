from datetime import datetime
from pytz import timezone

FORMAT = "%Y-%m-%d %H%M"
TIME_ZONE = 'Europe/Paris'

def current_time_zone_info():
    current_time = datetime.now(timezone(TIME_ZONE)).strftime(FORMAT)
    return current_time.split()
