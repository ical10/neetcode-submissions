class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    ## nums can be unsorted, so two pointers approach won't work.
    ## An alternative to keep O(n) time- and space-complexity is by using a hash map.
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

