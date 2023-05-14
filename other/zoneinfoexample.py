from datetime import datetime
from zoneinfo import ZoneInfo

# Create a datatime object with a speccific time
dt = datetime(2023, 5 , 1, 12, 0, tzinfo=ZoneInfo("America/New_York"))

# Convert the datetime object to a different time zone
new_york_tz = ZoneInfo("America/New_York")
london_tz = ZoneInfo("Europe/London")
london_time = dt.astimezone(london_tz)

# Print the original and convert time
print("New York Time: ", dt)
print("London Time: ", london_time)

