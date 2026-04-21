class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ansArr = [0]*n*2

        for idx, num in enumerate(nums):
            ansArr[idx] = num
            ansArr[n+idx] = num
        
        return ansArr