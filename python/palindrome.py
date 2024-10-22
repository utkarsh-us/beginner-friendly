"""I am using string slicing method to do this check, i know one more method that is using recursion that i have commented down feel free to edit and contribute <3"""

# main code
def is_palindrome(n):
    return n == n[::-1] # if n == reversed n

n = input() # user will give input
print(is_palindrome(n))  # calling the function and then printing boolean - True or False



"""
RECURSION METHOD!

def is_palindrome(n):
    if len(n) <= 1: # number of characters in n
        return True
    if n[0] != n[-1]: # if first character not equal to last character
        return False
    return is_palindrome(s[1:-1]) # if second character == second last character

# usage

n = input()
print(is_palindrome(n))

"""

