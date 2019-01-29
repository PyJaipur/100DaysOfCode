"""
A problem in which we have to find out the longest palindromic substring from the given string
"""


"""
First approach is to generate all the possible substring and check if it is the palindrome and it is longest
if yes return it

it will take O(n^3) time and O(1) space
"""

def longestpalindrome(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if(len(substring)>len(longest)) and isPlalindrome(substring):
                longest = substring
    return longest


def isPlalindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


print(longestpalindrome("abaxyzzyxf"))


"""
Second approach is more optimal then the first approach, as it run in O(n^2) time rather then in
O(n^3)
"""


def getLongestPalindrome(data, left, right):
    while left >= 0 and right < len(data):
        if data[left] != data[right]:
            break
        left -= 1
        right += 1
    return [left + 1, right]


def optimalpalindrome(data):
    currentLongest = [0, 1]
    for i in range(1, len(data)):
        odd = getLongestPalindrome(data, i-1, i+1)
        even = getLongestPalindrome(data, i-1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key=lambda x: x[1]-x[0])
    return data[currentLongest[0]:currentLongest[1]]


print(optimalpalindrome("abaxyxxyxf"))

