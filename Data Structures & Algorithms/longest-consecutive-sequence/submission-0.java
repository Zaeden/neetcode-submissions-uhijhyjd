class Solution {
    public int longestConsecutive(int[] nums) {
        int n = nums.length;
        int count = 0, len = 0;
        HashSet<Integer> set = new HashSet<>();
        for(int num: nums) {
            set.add(num);
        }
        for(int num: nums) {
            int prevElement = num - 1;
            if(!set.contains(prevElement)) {
                len = 1;
                int nextElement = num + 1;
                while(set.contains(nextElement)) {
                    len++;
                    nextElement++;
                }
            }
            count = Math.max(len, count);
        }
        return count;
    }
}
