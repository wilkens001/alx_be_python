# Global conversion factors
CELSIUS_TO_FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
FAHRENHEIT_TO_CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return CELSIUS_TO_FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    return (FAHRENHEIT_TO_CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

def main():
    # Get temperature from user
    try:
        user_input = input("Enter the temperature to convert: ")
        if not user_input.replace('.', '', 1).replace('-', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        temp = float(user_input)
    except ValueError as e:
        print(str(e))
        return

    # Get temperature unit from user
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if unit not in ['C', 'F']:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        return

    # Perform conversion based on input unit
    try:
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")
        else:  # unit == 'F'
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")
    except Exception:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()