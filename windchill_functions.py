# This function calculates and return the wind chill
def calculate_windchill(temperature_fahrenheit, speed_check):
    wind_chill = 35.74 + (0.6215 * temperature_fahrenheit) - 35.75 * (speed_check ** 0.16) + 0.4275 * temperature_fahrenheit * (speed_check ** 0.16)
    return wind_chill
# This function converts values entered in celsius to fahrenheit
def convert_to_fahrenheit(celsius):
    return(celsius * 9/5) + 32


# This allows a user to enter a temperature and it's scale
temperature = float(input("What is the temperature? ")) 
scale_for_temperature = input("Fahrenheit or Celsius (F/C)? ")

if scale_for_temperature.lower() == "c":
    temperature_fahrenheit = convert_to_fahrenheit(temperature)

else:
    temperature_fahrenheit = temperature


# This Loops through wind speeds and calculates wind chill
wind_speeds = range(5, 61, 5)
for speed_check in wind_speeds:
    wind_chill = calculate_windchill(temperature_fahrenheit, speed_check)
    print(f"At temperature {temperature_fahrenheit:.2f}F, and wind speed {speed_check}mph, the windchill is: {wind_chill:.2f}F ")