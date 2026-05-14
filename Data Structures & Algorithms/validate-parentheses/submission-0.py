class Solution:
    def isValid(self, s: str) -> bool:
        bucket = {')':'(', ']':'[','}':'{',}
        stack = []
        for char in s:
            if char in bucket:
                top_elem = stack.pop() if stack else '#'
                if bucket[char]!= top_elem:
                    return False
            else:
                stack.append(char)
        return len(stack)==0