class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False


#
# 64 ms
# 17.6 MB

# class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#        sCount, tCount = Counter(s), Counter(t)
#        return sCount == tCount
