from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        
        for i in count.most_common(k):
            res.append(i[0])

        return res