
#  Program to check given number is palindrome
check_palindrome = input('Please a numbet to check palindrome \n')

reversed_string = "".join(reversed(check_palindrome))

if(check_palindrome == reversed_string):
    print("Palindrome")
else:
    print("Not a palindrome")

