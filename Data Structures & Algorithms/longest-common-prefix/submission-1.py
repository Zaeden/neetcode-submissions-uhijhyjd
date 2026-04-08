class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        n = len(strs[0])
        first, last = strs[0], strs[-1]
        min_length = min(len(first), len(last))
        prefix = -1
        for i in range(min_length):
            if first[i] == last[i]:
                prefix += 1
            else:
                break
        return first[:prefix + 1]