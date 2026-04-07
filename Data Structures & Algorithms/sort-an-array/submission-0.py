class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums, low, mid, high):
            temp = []
            left = low
            right = mid + 1

            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            
            while left <= mid:
                temp.append(nums[left])
                left += 1

            while right <= high:
                temp.append(nums[right])
                right += 1

            i = low
            while i < high + 1:
                nums[i] = temp[i - low]
                i += 1

        def merge_sort(nums, low, high):
            # Base Case
            if low >= high:
                return
            mid = (low + high) //2
            merge_sort(nums, low, mid)
            merge_sort(nums, mid+1, high)
            merge(nums, low, mid, high)
        
        merge_sort(nums, 0, len(nums) - 1)
        return nums