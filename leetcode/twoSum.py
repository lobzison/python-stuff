class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for idx, num in enumerate(nums):
            complement = target - num
            found = h.get(complement)
            if found is not None:
                return [found, idx]
            h[num] = idx
