class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}
        for s in strs:
            sorted_s = sorted(s)
            key = tuple(sorted_s)

            if key not in result:
                result[key]=[s]
            else:

                result[key].append(s)
        return list(result.values())

