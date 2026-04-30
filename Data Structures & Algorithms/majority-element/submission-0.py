class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashset = {}
        item = 0
        for i in nums:
            if i in hashset:
                hashset[i] +=1
            else: hashset[i] = 1
        for i in hashset:
            if hashset[i] > len(nums)/2:
                return i



