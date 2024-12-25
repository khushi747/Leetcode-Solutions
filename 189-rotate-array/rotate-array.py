         
class Solution:
    def rotate(self, a:List[int], k:int)-> None:
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(a)
        if n==1:
            return
        k = k % len(a)
        def reverse(start:int ,end:int) -> None:
            while(start<end):
                a[start],a[end]=a[end],a[start]
                start=start+1
                end-=1
                

        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)