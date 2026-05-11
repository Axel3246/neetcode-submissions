class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        count = 0

        for num in numSet:
            if num - 1 not in numSet:
                currCnt = 1
                nextVal = num + 1
                while nextVal in numSet:
                    currCnt += 1
                    nextVal += 1
                count = max(count, currCnt)
        
        return count