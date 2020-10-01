def isPalindrome(s):
    return s == s[::-1]
 

s = input("Enter a string:")
rs = isPalindrome(s)
 
if rs:
    print(rs "is a Palindrome")
else:
    print("Not a Palindrome")
