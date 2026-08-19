class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for x in range(len(s)):
            count[s[x]] = count.get(s[x],0) + 1
            count[t[x]] = count.get(t[x],0) - 1

        for value in count.values():
            if value != 0:
                return False
        return True



        
        
    
    