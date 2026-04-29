class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}
        for s in strs:
            s_sorted = sorted(s)
            key = tuple(s_sorted)

            if key not in result:
                result[key] = [s]
            else: 
                result[key].append(s)

        return list(result.values())