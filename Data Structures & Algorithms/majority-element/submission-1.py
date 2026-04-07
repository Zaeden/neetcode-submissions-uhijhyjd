class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority_element = 0

        for i in nums:
            if count == 0:
                count = 1
                majority_element = i
            elif i == majority_element:
                count += 1
            elif i != majority_element:
                count -= 1
            
        
        return majority_element