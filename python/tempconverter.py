# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to handle user choice and perform the conversion
def temperature_converter():
    # Display conversion options
    print("Select the type of conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    # Take user input for the choice
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        # Celsius to Fahrenheit conversion
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
    
    elif choice == 2:
        # Fahrenheit to Celsius conversion
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")
    
    else:
        print("Invalid choice! Please enter 1 or 2.")

# Call the temperature converter function
temperature_converter()
