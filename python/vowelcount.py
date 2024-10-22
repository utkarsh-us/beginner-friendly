# Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    
    # Iterate through each character and check if it's a vowel
    for char in s:
        if char in vowels:
            count += 1
    return count

# Take user input for the string
s = input("Enter a string: ")

# Call the function and print the result
print("Number of vowels in the string:", count_vowels(s))
