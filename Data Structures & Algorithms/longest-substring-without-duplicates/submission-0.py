class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        max_count =0 
        substring =''  
        while j <len(s):
            if s[j] not in substring:
                substring = substring+s[j]
                count = len(substring)
                max_count = max(max_count,count)
                j+=1
            else:
                substring = substring[1:]
                i+=1
        return max_count