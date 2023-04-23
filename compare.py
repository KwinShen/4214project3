import smbus2
import bme280
import time


port = 1
address = 0x77
bus = smbus2.SMBus(port)


calibration_params = bme280.load_calibration_params(bus, address)

with open("/sys/bus/iio/devices/iio:device0/in_voltage2_raw") as f:
    while True:
        data = bme280.sample(bus, address, calibration_params)
        time_string = data.timestamp.strftime("%H:%M:%S")
        temperature = "{:.2f}".format(data.temperature)
    
        print("Time:", time_string)
        print("BME280 Temperature:", temperature, "°C")

        print("ADC counts(RTD): ",f.read())
        f.seek(0)
    
        print("-"*30)
        time.sleep(1)