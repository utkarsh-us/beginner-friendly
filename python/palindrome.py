# Main code with string slicing
def is_palindrome(n):
    return n == n[::-1]  # Check if n is equal to its reverse

n = input("Enter a string: ")  # User input
print(is_palindrome(n))  # Calling the function and printing True or False


"""
RECURSION METHOD
Feel free to edit and contribute <3
"""

# Recursive method to check palindrome
def is_palindrome_recursive(n):
    if len(n) <= 1:
        return True
    if n[0] != n[-1]:
        return False
    return is_palindrome_recursive(n[1:-1])

# Uncomment this to use the recursive method:
# n = input("Enter a string: ")
# print(is_palindrome_recursive(n))
