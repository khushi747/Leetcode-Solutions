class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        j=0
        i=0
        while(i<n):
            if(nums[i]==0 and nums[j]==0):
                i=i+1
            elif(nums[i]!=0):
                nums[i],nums[j]=nums[j],nums[i]
                i=i+1
                j=j+1
            else:
                i=i+1
                
