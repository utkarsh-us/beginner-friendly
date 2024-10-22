# Function to check if a number is odd or even
def check_odd_even(number):
    # A number is even if divisible by 2, otherwise it's odd
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Input from the user
number = int(input("Enter a number: "))

# Check if it's odd or even and display the result
result = check_odd_even(number)
print(f"{number} is {result}.")
