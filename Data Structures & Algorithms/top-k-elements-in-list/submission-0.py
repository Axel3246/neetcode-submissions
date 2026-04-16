class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        ans = list(hmap.items())
        ans.sort(key=lambda t:t[1], reverse=True)

        return [key[0] for key in ans[:k]]