class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in range(len(nums)):
            count[nums[x]] = count.get(nums[x], 0) + 1

        return sorted(count, key = count.get, reverse = True)[:k]
