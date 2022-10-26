import datetime

current_time = datetime.datetime.utcnow()

interval_end_time = current_time - datetime.timedelta(
    minutes=current_time.minute % 5,
    seconds=current_time.second,
    microseconds=current_time.microsecond)

interval_start_time = interval_end_time - datetime.timedelta(minutes=5)

print("Start Interval Time: " + interval_start_time.isoformat())
print("End Interval Time: " + interval_end_time.isoformat())

print("Start Interval Time: " + interval_start_time.strftime('%Y-%m-%dT%H:%M:%SZ'))
print("End Interval Time: " + interval_end_time.strftime('%Y-%m-%dT%H:%M:%SZ'))