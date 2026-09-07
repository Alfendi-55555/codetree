A = input()

# Please write your code here.

def is_palindrome(s):
    palindrome = A[::-1]
    if palindrome == s:
        print("Yes")
    else:
        print("No")

is_palindrome(A)