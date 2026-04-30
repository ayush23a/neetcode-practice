class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        count = 0
        for i in nums:
            if i != val:
                nums[j] = i
                j +=1
            else: count +=1
        
        k = len(nums) - count
        return k


