class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxcount=0
        for i in range(len(nums)):
            if(nums[i]==1):
                count=count+1
            if(nums[i]==0):
                maxcount=max(maxcount,count)
                count=0
        maxcount=max(count,maxcount)
        return maxcount
        