class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)
        for i in nums:
            if i in freq:
                freq[i] += 1
            elif i not in freq:
                freq[i] = 1
            
            if freq[i] > n/2:
                return i