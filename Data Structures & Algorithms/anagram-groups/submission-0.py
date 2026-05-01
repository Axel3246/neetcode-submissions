class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr in hmap:
                hmap[sortedStr].append(s)
            else:
                hmap[sortedStr] = [s]
        
        return list(hmap.values())
