def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
      
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = check_even_odd(number)
    print(f"The number {number} is {result}.")
