# A simple problem of checking if the given string a palindrome or not.
# Author Sidhant Rajora


# A simple solution is to like, create a reverse of the string and match it with the
# original string


def isPalindrome(string):
    # Write your code here.
    return string == string[::-1]


# In this approach the reverse of string is need to be created(or iterated over) and
# that's an extra overhead

# So in second approach we can have two pointers, pointing to start of the string
# and end of the string, and will keep on checking until we reach the middle of the string
# and all goes well we return true, and at any particular point mismatch occurs we can
# return false


def isPalindrome2(string):
    left = 0
    right = len(string) - 1
    while (left < right):
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True
