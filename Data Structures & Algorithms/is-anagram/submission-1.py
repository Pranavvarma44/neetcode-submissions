class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        x={}
        for i in s:
            x[i]=x.get(i,0)+1
        for j in t:
            if j not in x or x[j]==0:
                return False
            x[j]-=1
        return True
