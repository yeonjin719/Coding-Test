class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        TDict = {}
        for i in t:
            if (i in TDict):
                TDict[i] += 1
            else:
                TDict[i] = 1
        TKeys = TDict.keys()
        for i in TKeys:
            if i not in s:
                return False
            if (s.count(i) != TDict[i]):
                return False
        return True

solution = Solution()
s = "anagram"
t = "nagaram"
result = solution.isAnagram(s, t)
print(result)  # Output: True