str1 = input("Enter the string:")
str1 = str1.casefold()
rev_str = reversed(str1)

if list(str1) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
