class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let n = nums.length;
        let seen = {};
        for (let i = 0; i < n; i++) {
            if (target - nums[i] in seen) {
                return [ seen[target - nums[i]], i ];
            }
            seen[ nums[i] ] = i;
        }
        return [];
    }
}
