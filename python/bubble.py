# Function to perform Bubble Sort on an array
def bubble_sort(arr):
    n = len(arr)  # Get the length of the array

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so skip them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Perform the swap

# Take input from the user as a space-separated list of numbers
arr = list(map(int, input("Enter numbers to sort (space-separated): ").split()))

# Print the array before sorting
print("Array before sorting:", arr)

# Call the bubble_sort function
bubble_sort(arr)

# Print the sorted array
print("Array after sorting:", arr)
