import pendulum

# Create a Pendulum datetime object
dt = pendulum.datetime(2023, 5, 14, tz='America/New_York')

# Manipulate the datetime object
dt = dt.add(days=1).subtract(hours=3)

# Display the datetime object in a specific format
formatted = dt.format('YYYY-MM-DD HH:mm:ss')
print(formatted)
