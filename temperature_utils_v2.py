from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    celsius = float(fahrenheit_temp - 32) * 5/9

    return float(round(celsius, 2))



def convert_to_kelvin(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    kelvin = float(celsius_temp + 273.15)

    return float(round(kelvin, 2))






def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    fahrenheit = float(celsius_temp * 1.8) + 32

    return float(round(fahrenheit, 4))



def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    x = []

    for temp in temperatures:
        if input_unit_of_measurement == "f":
            t = convert_to_celsius(temp)
            t2 = (temp,t)
            x.append(t2)
        elif input_unit_of_measurement == "c":
            y = convert_to_fahrenheit(temp)
            y2 = (temp,y)
            x.append(y2)
        elif input_unit_of_measurement == "k":
            kel1 = convert_to_kelvin(temp)
            kel2 = (temp,kel1)
            x.append(kel2)
    return tuple(x)