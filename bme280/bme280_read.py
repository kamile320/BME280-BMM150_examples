import smbus2, bme280 #requirements

ver=1.0
port=1
address=0x76
bus=smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

def read_all():
    data = bme280.sample(bus, address, calibration_params)
    return (
        data.temperature,
        data.pressure,
        data.humidity,
        data.timestamp,
        data.id
    )

def id():
    data = bme280.sample(bus, address, calibration_params)
    return data.id

def timestamp():
    data = bme280.sample(bus, address, calibration_params)
    return data.timestamp

def temperature():
    data = bme280.sample(bus, address, calibration_params)
    return round(data.temperature,2)#°C

def pressure():
    data = bme280.sample(bus, address, calibration_params)
    return round(data.pressure,2)#hPa

def humidity():
    data = bme280.sample(bus, address, calibration_params)
    return round(data.humidity,2)#rH
