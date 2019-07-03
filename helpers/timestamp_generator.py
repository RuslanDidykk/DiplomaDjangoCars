from datetime import datetime

def generate_timestamp(format="%Y.%m.%d:%H:%M:%S"):
    timestamp = datetime.strftime(datetime.now(), format)
    return timestamp