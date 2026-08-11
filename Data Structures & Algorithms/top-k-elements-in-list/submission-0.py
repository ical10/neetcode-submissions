class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. create n buckets, from 1 to n
        # 2. pick the top k from the buckets, starting from n down to 1.

        count = {}
        # fill in the bucket with the frequency of each val in nums
        for n in nums:
            count[n] = count.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for n, freq in count.items():
            buckets[freq].append(n)

        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for n in buckets[freq]:
                result.append(n)

                if len(result) == k:
                    return result

        
        