from datetime import datetime
import pytz

def get_date():
    return datetime.utcnow().replace(tzinfo=pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d')

def get_time(iso8601):
    date_time = datetime.strptime(iso8601, "%Y-%m-%dT%H:%M:%S%z")
    return date_time.time().strftime("%H:%M")

def get_percents(list):
    result = []
    for item in list:
        result.append(round(item / sum(list) * 100))
    return result

def try_parse_int(text):
    try:
        value = int(text)
        return True
    except:
        return None

def try_parse_float(text):
    try:
        to_float = float(text)
        return True
    except:
        return None

def try_calculate(text):
    try:
        return eval(text)
    except:
        return None