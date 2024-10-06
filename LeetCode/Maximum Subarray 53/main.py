
class Solution:
    def maxSubArray (self, nums: List[int]) -> int:
        maxSub = nums[0]
        cursum = 0
         
        for n in nums:
            if cursum < 0:
                cursum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub