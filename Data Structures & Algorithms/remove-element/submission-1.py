class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums:
            return len(nums)

        L, R = 0, 1

        while R < len(nums):
            if nums[L] == val and nums[R] != val:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
                R += 1
            elif nums[L] == val and nums[R] == val:
                R += 1
            else:
                L += 1
                R += 1
        
        return L