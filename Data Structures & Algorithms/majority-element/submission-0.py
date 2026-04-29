class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        return max(hmap, key=hmap.get)