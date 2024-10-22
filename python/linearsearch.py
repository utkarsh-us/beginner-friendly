def linear_search(lst, target):
    # Iterate through the list
    for i in range(len(lst)):
        # Check if the current element matches the target
        if lst[i] == target:
            return i  # Return the index of the target element
    return -1  # Return -1 if the target is not found

# Example usage
my_list = [10, 20, 30, 40, 50]
target = 30
result = linear_search(my_list, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
