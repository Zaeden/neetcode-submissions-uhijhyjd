class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s in mp:
                mp[sorted_s].append(s)
            else:
                mp[sorted_s] = [s]
            
        result = []
        for key in mp:
            result.append( mp[key] )
        return result