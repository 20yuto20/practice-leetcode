############################################################
# 28. Find the Index of the First Occurrence in a String
############################################################
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    

# OR

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n= len(haystack)
        m= len(needle)
        
        if m > n:
            return -1
        
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
        return -1