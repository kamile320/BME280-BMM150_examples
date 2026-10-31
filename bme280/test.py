import bme280_read

#Testing

print(bme280_read.timestamp())

print(bme280_read.humidity())
print(bme280_read.pressure())
print(bme280_read.id())
print(bme280_read.temperature())


temp, press, hum, time, id = bme280_read.read_all()


print(temp)
print(press)
print(hum)
print(time)
print(id)
