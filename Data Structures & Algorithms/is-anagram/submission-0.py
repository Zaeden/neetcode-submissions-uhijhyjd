class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)
        seen = {}

        if ns != nt:
            return False
        
        for key in s:
            if key in seen:
                seen[key] = seen[key] + 1
            else:
                seen[key] = 1
        
        for key in t:
            if key in seen:
                seen[key] = seen[key] - 1

        for key in seen:
            if(seen[key] != 0):
                return False

        return True    