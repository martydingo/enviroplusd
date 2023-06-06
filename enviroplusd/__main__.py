    bme280_data = sensors.BME280().poll()

    climate = {
        "temperature": bme280_data["temperature"],
    }

    print(climate)
