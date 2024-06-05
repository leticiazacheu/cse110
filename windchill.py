def calculate_wind_chill(temp_f, wind_speed):
    # Calculate wind chill using the given temperature in Fahrenheit and wind speed in miles per hour.
    wind_chill = 35.74 + 0.6215 * temp_f - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp_f * (wind_speed ** 0.16)
    return round(wind_chill, 2)

def celsius_to_fahrenheit(temp_c):
    # Convert temperature from Celsius to Fahrenheit.
    temp_f = temp_c * (9/5) + 32
    return temp_f

def main():
    # Main function to prompt the user for temperature input and display wind chill for various wind speeds.
    temp_str = input("What is the temperature? ")
    temp_unit = input("Fahrenheit or Celsius (F/C)? ").upper()

    temp = float(temp_str)

    if temp_unit == 'C':
        temp = celsius_to_fahrenheit(temp)

    print(f"At temperature {temp}{temp_unit}, and wind speed:")

    for wind_speed in range(5, 61, 5):
        wind_chill = calculate_wind_chill(temp, wind_speed)
        print(f"    {wind_speed} mph, the windchill is: {wind_chill}{temp_unit}")

    # Creative touch: Encourage users to bundle up if it's cold
    if temp < 32:
        print("Brrr! It's cold outside! Don't forget to bundle up!")
    elif temp > 80:
        print("Wow, it's hot out there! Remember to stay hydrated and wear sunscreen!")
    else:
        print("Looks like a pleasant day! Enjoy the weather!")

if __name__ == "__main__":
    main()