class Solution:
    def isValid(self, s: str) -> bool:
        # bucket = {')':'(', ']':'[','}':'{',}
        # stack = []
        # for char in s:
        #     if char in bucket:
        #         top_elem = stack.pop() if stack else '#'
        #         if bucket[char]!= top_elem:
        #             return False
        #     else:
        #         stack.append(char)
        # return len(stack)==0
        bucket = { ')':'(',
                    '}':'{',
                    ']':'[',
                    }
        stack = []
        for i in s:
            if i in bucket:
                top_element = stack.pop() if stack else '#'
                if bucket[i] != top_element:
                    return False
            else:
                stack.append(i)
        return len(stack)==0