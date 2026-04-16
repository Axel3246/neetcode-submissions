class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0]*n*2
        for i,v in enumerate(nums):
            arr[i] = v
            arr[n+i] = v
        
        return arr
