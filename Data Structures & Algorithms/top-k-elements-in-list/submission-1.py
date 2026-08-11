class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. create n buckets, from 1 to n
        # 2. pick the top k from the buckets, starting from n down to 1.

        count = {}

        # register the unique count of each num
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # initialize the buckets, containing subarrays of int with same frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        # traverse count, fill in subarrays with int
        for num, freq in count.items():
            buckets[freq].append(num)

        # traverse buckets, from top to bottom, until top-k is reached
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result
        
        
        