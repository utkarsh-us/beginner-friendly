
# Function to print Fibonacci series up to a given limit
def fibonacci_series(limit):
    # Initialize the first two numbers of the series
    a, b = 0, 1
    
    # Print the first number
    print("Fibonacci series up to", limit, ":")
    print(a, end=" ")

    # Loop to generate the series until the limit is reached
    while b <= limit:
        print(b, end=" ")  # Print the next number
        a, b = b, a + b    # Update the values for the next iteration

# Take input from the user for the limit
user_limit = int(input("Enter the limit for the Fibonacci series: "))

# Call the function to print the Fibonacci series
fibonacci_series(user_limit)
