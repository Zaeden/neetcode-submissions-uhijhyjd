class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for i in strs:
            sorted_string = "".join(sorted(i))
            
            if sorted_string in mp:
                mp[sorted_string].append(i)
            else:
                mp[sorted_string] = [i]
        result = []
        for key in mp:
            result.append(mp[key])
        return result