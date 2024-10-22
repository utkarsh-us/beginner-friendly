# Function to calculate Simple Interest
def calculate_simple_interest(principal, rate, time):
    # Formula for simple interest: SI = (P * R * T) / 100
    interest = (principal * rate * time) / 100
    return interest

# Input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time (in years): "))

# Calculate simple interest
interest = calculate_simple_interest(principal, rate, time)

# Output the result
print(f"Simple Interest for the given values is: {interest}")
