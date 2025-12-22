# Smart Thermostat Decision Maker

device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High Temperature Alert!")
    else:
        print("Temperature is Normal.")
else:
    print("Device is Offiline")