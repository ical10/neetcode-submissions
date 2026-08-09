class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        // using two pointers
        // Time complexity: O(N), space complexity: O(1)
        let left = 0;
        for (let right = 1; right < nums.length; right++) {
            if (nums[left] !== nums[right]) {
                left++;
                nums[left] = nums[right];
            } else {
                continue;
            }
        }
        return left + 1;
    }
}
