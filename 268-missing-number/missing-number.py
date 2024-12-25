class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
        ans= (n*(n+1))//2-s
        return ans