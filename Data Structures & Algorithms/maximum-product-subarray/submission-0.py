class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        prefix, suffix = 0, 0
        for i in range(len(nums)):
            if prefix == 0: prefix = 1
            if suffix == 0: suffix = 1

            prefix *= nums[i]
            suffix *= nums[len(nums) - 1 - i]
            res = max(res, prefix, suffix)

        return res