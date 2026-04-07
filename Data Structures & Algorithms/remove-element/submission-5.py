class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if not n:
            return 0

        i = 0
        while i < n and nums[i] != val:
            i += 1

        j = i + 1
        while( j < n):
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        print(nums)
        return i 