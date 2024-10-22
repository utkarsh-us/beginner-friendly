# Function to count the frequency of elements in a list
def count_frequency(arr):
    # Dictionary to store frequency of each element
    frequency = {}
    
    # Loop through the list and count occurrences of each element
    for item in arr:
        if item in frequency:
            frequency[item] += 1  # Increment count if the item is already in the dictionary
        else:
            frequency[item] = 1  # Add the item to the dictionary with a count of 1
    
    return frequency

# Input: list of elements from the user
arr = input("Enter elements separated by spaces: ").split()

# Get the frequency count
frequency = count_frequency(arr)

# Display the frequency of each element
for key, value in frequency.items():
    print(f"{key}: {value}")
