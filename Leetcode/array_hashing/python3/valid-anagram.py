class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


#
# 64 ms
# 17.6 MB

# class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#        sCount, tCount = Counter(s), Counter(t)
#        return sCount == tCount
