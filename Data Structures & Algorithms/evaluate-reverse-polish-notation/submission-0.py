import operator
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dic ={
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '/': lambda a ,b : int(a/b) }
        stack = []
        for token in tokens:
            if token in dic :
                b = stack.pop()
                a = stack.pop()
                result = dic[token](a,b)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]

        