import time
import sys

sys.setrecursionlimit(2147483647)

def countdown(n):
    if n == 0:
        print("BOOOOOOM!", end="")
    else:
        print(n)
        time.sleep(1)
        countdown(n - 1)

def reverse_string(s):
    if (s == ""):
        print()
    else:
        print(s[len(s) - 1], end="")
        reverse_string(s[0:len(s) - 1])

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def remove_char(s, c):
    if (s == ""):
        return ""
    if s[0] == c:
        return remove_char(s[1:], c)
    return s[0] + remove_char(s[1:], c)

def power_4(n):
    n /= 4
    if n == 1:
        return True
    if n < 1:
        return False
    return power_4(n)

def is_palindrome(w):
    if len(w) == 1 or len(w) == 0:
        return True
    if w[0] == w[len(w) - 1]:
        return is_palindrome(w[1:len(w) - 1])
    return False

def permutations(s):
    pass
def calc_exp(b, e):
    if e == 1:
        return b
    return b * calc_exp(b, e - 1)
def digit_1(n):
    if n <= 0:
        return 0

    ones = 0
    temp_n = n
    while temp_n > 0:
        if temp_n % 10 == 1:
            ones += 1
        temp_n = int(temp_n / 10)
    
    return ones + digit_1(n - 1)

def gcd(n1, n2, div = 1, max = 1):
    if n1 % div == 0 and n2 % div == 0:
        max = div
    if div == n1 or div == n2:
        return max
    return gcd(n1, n2, div + 1, max)        

def find_paths(m):
    pass
def binary_string(n):
    pass

if __name__ == "__main__":
    while True:
        print("""
1. Countdown
2. Reverse String
3. Factorial
4. Remove Char
5. Power of 4
6. Is Palindrome
7. Permutations
8. Calculate Exponent
9. Digit 1
10. Greatest Common Divisor
11. Find Paths
12. Binary String   
Q. Quit
""")
        selection = input("Enter a selection: ")

        if selection == "1":
            n = int(input("Enter a number to count down from: "))
            countdown(n)
        elif selection == "2":
            s = input("Enter a string to reverse: ")
            reverse_string(s)
        elif selection == "3":
            n = int(input("Enter a number to find the factorial of: "))
            print(factorial(n))
        elif selection == "4":
            s = input("Enter a string: ")
            c = input("Enter a character to remove: ")
            print(remove_char(s, c))
        elif selection == "5":
            n = int(input("Enter a number to check if it is a power of 4: "))
            print(power_4(n))
        elif selection == "6":
            w = input("Enter a word to check if it is a palindrome: ")
            print(is_palindrome(w.lower()))
        elif selection == "7":
            pass
        elif selection == "8":
            n = int(input("Enter a base: "))
            e = int(input("Enter an exponent: "))
            print(calc_exp(n, e))
        elif selection == "9":
            n = int(input("Enter a number to count the number of 1's: "))
            print(digit_1(n))
        elif selection == "10":
            n1 = int(input("Enter the first number: "))
            n2 = int(input("Enter the second number: "))
            print(gcd(n1, n2))