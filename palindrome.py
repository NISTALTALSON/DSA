class Solution:
    def isPalindrome(self, x):
        s = str(x)
        r = s[::-1]
        return s == r

