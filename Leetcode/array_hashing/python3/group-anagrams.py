from typing import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        else:
            anagramDict = {}
            for word in strs:
                sortedWord = "".join(sorted(word))
                if sortedWord in anagramDict:
                    anagramDict[sortedWord].append(word)
                else:
                    anagramDict[sortedWord] = [word]
            return list(anagramDict.values())
