class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrome = 0
        number = x
        while number > 0:
            palindrome = palindrome * 10 + number % 10
            number //= 10
        return x == palindrome


fun = Solution()
print(fun.isPalindrome(121))
