import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if plugged:
    print(f"Зарядка поделючена, заряд батареи: {percent}%")
else:
    print(f"Зарядка отключена, заряд батареи: {percent}%")
