import random
from abc import ABC, abstractmethod

class Probe:

    def get_temperature(self):
        return random.randint(-20, 40)

    def get_humidity(self):
        return random.randint(0, 100)

    def get_pressure(self):
        return random.randint(700, 1200)

class Display(ABC):

    @abstractmethod
    def update_display(self, temperature, humidity, pressure):
        pass

class CurrentWeatherDisp(Display):

    def update_display(self, temperature, humidity, pressure):
        print(f'{temperature} °C {humidity} % {pressure} hPa update current weather display')

class ForecastWeatherDisp(Display):

    def update_display(self, temperature, humidity, pressure):
        print(f'{temperature} °C {humidity} % {pressure} hPa update forecast for ...')

class StatsDisp(Display):

    def update_display(self, temperature, humidity, pressure):
        print(f'{temperature} °C {humidity} % {pressure} hPa stats display')


class WeatherStation:

    def __init__(self, probe: Probe):
        self.__probe = probe
        self.__displays = []

    def add_display(self, display: Display):
        self.__displays.append(display)

    def get_display(self):
        return self.__displays

    def measurements_changed(self):
        # get measurements from probe
        temperature = self.__probe.get_temperature()
        humidity = self.__probe.get_humidity()
        pressure = self.__probe.get_pressure()

        for display in self.get_display():
            display.update_display(temperature, humidity, pressure)


if __name__ == '__main__':
    weather_station = WeatherStation(Probe())
    weather_station.add_display(CurrentWeatherDisp())    
    weather_station.add_display(ForecastWeatherDisp())
    weather_station.add_display(StatsDisp())
    weather_station.measurements_changed()
    weather_station.add_display(StatsDisp())
    weather_station.measurements_changed()
