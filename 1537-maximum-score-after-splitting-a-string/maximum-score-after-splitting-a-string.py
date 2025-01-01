class Solution:
    def maxScore(self, s: str) -> int:
        onescount=0
        zeroscount=0
        n=len(s)
        count=0
        maxcount=0
        for i in range(n):
            if s[i]=='1':
                onescount=onescount+1
        for i in range(n-1):
            if(s[i]=="0"):
                zeroscount=zeroscount+1
            if(s[i]=="1"):
                onescount=onescount-1
            count=onescount,zeroscount
            maxcount=max(maxcount,onescount+zeroscount)
        return maxcount
                