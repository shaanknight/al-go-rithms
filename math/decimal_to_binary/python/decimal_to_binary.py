def decimal_to_binary(n):
    if n > 1: decimal_to_binary(n//2)
    print(n % 2, end = '')

try: num = int(input("Enter an Integer to Convert into Binary: "))
except ValueError: print("Input is not an integer.")
decimal_to_binary(num)
print()
