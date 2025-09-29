# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = -32
CELSIUS_TO_FAHRENHEIT_FACTOR = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius."""
    return (fahrenheit + FAHRENHEIT_TO_CELSIUS_FACTOR) * (5/9)

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * (9/5)) + CELSIUS_TO_FAHRENHEIT_FACTOR

def main():
    try:
        # Get temperature from user
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    # Get temperature unit from user
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    # Perform conversion based on input unit
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()