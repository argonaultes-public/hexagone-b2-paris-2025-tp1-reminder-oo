import random


class Probe:

    def get_temperature(self):
        return random.randint(-20, 40)

    def get_humidity(self):
        return random.randint(0, 100)

    def get_pressure(self):
        return random.randint(700, 1200)

class CurrentWeatherDisp:

    def update_weather_disp(temperature, humidity, pressure):
        print('update current weather display')

class ForecastWeatherDisp:

    def update_forecast_disp(temperature, humidity, pressure):
        print('update forecast for ...')

class StatsDisp:

    def update_stats_disp(temperature, humidity, pressure):
        print('stats display')


class WeatherStation:

    def __init__(self, probe: Probe, current_weather, forecast_weather, stats_weather):
        self.__probe = probe
        self.__current_weather = current_weather
        self.__forecast_weather = forecast_weather
        self.__sats_weather = stats_weather

    #TODO
    def measurements_changed(self):
        pass