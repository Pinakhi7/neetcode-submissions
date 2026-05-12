class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if c.isalnum()]).lower()
        strings = s[::-1]
        if s == strings:
            return True
        return False