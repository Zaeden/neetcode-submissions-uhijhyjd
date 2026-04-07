class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        for i in range(n):
            if ( target - nums[i] ) in seen:
                result = [seen[ target - nums[i] ], i]
                break
            else:
                seen[nums[i]] = i
        return result
        