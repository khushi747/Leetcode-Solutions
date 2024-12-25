class Solution(object):
    
    def check(self,arr):
        n=len(arr)
        count=0
        for i in range(0,n):
            if(arr[i]>arr[(i+1)%n]):
                count=count+1
        return count<=1
            