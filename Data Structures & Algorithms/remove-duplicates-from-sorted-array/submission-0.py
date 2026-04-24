class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        seen = set()
    
        # To maintain the new size of the array
        idx = 0

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[idx] = nums[i]
                idx += 1

        # Return the size of the array 
        # with unique elements
        return idx


