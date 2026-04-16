class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ms = set()

        for num in nums:
            if num in ms:
                return True
            ms.add(num)
        
        return False