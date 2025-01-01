class Solution:
    def maxScore(self, s: str) -> int:
        count=0
        maxcount=0
        n=len(s)
        for i in range(n-1):
            count=0
            left=s[0:i+1]
            right=s[i+1:n]
            for j in range(len(left)):
                if(left[j]=='0'):
                    count=count+1
            for k in range(len(right)):
                if(right[k]=='1'):
                    count=count+1
            maxcount=max(maxcount,count)

        return maxcount
                