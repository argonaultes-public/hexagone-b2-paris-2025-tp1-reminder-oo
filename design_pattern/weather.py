import random


class Probe:

    def get_temperature(self):
        return random.randint(-20, 40)

    def get_humidity(self):
        return random.randint(0, 100)

    def get_pressure(self):
        return random.randint(700, 1200)

class CurrentWeatherDisp:

    def update_weather_disp(self, temperature, humidity, pressure):
        print(f'{temperature} °C {humidity} % {pressure} hPa update current weather display')

class ForecastWeatherDisp:

    def update_forecast_disp(self, temperature, humidity, pressure):
        print(f'{temperature} °C {humidity} % {pressure} hPa update forecast for ...')

class StatsDisp:

    def update_stats_disp(self, temperature, humidity, pressure):
        print(f'{temperature} °C {humidity} % {pressure} hPa stats display')


class WeatherStation:

    def __init__(self, probe: Probe, current_weather, forecast_weather, stats_weather):
        self.__probe = probe
        self.__current_weather = current_weather
        self.__forecast_weather = forecast_weather
        self.__stats_weather = stats_weather


    def measurements_changed(self):
        # get measurements from probe
        temperature = self.__probe.get_temperature()
        humidity = self.__probe.get_humidity()
        pressure = self.__probe.get_pressure()

        self.__current_weather.update_weather_disp(temperature, humidity, pressure)
        self.__forecast_weather.update_forecast_disp(temperature, humidity, pressure)
        self.__stats_weather.update_stats_disp(temperature, humidity, pressure)

if __name__ == '__main__':
    weather_station = WeatherStation(Probe(), CurrentWeatherDisp(), ForecastWeatherDisp(), StatsDisp())
    weather_station.measurements_changed()