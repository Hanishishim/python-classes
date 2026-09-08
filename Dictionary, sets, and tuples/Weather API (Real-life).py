weather = {
    "city": "newyork",
    "main": {
        "temperature": 91,
        "humidity": 64
    },
    "wind": {
        "speed": 8
    }
}
print("City:", weather["city"])
print("Temperature:", weather["main"]["temperature"])
print("Humidity:", weather["main"]["humidity"])
print("Wind Speed:", weather["wind"]["speed"])
