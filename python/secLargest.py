# Function to find the second largest number in a list
def second_largest(arr):
    # Remove duplicates by converting to a set, then back to a list
    unique_numbers = list(set(arr))
    
    # Check if there are at least two unique numbers
    if len(unique_numbers) < 2:
        return None  # Return None if not enough elements
    
    # Sort the list in descending order and return the second element
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

# Input: list of numbers from the user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Find the second largest number
result = second_largest(arr)

# Display the result
if result is not None:
    print(f"The second largest number is: {result}")
else:
    print("Not enough unique numbers to find the second largest.")
