class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        sortedKeys = list(dict(sorted(hmap.items(), key= lambda item: item[1], reverse=True)))
        return sortedKeys[:k]
        