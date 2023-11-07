def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_to_reamur(celsius):
    reamur = celsius * 4/5
    return reamur

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

if __name__ == "__main__":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    reamur = celsius_to_reamur(celsius)
    kelvin = celsius_to_kelvin(celsius)

    print(f"Temperature in Fahrenheit is: {fahrenheit}°F")
    print(f"Temperature in Reamur is: {reamur}°Re")
    print(f"Temperature in Kelvin is: {kelvin}K")
