class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        answer  = 0
        seen = set()

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            answer = max(answer, i - left + 1)

            
        return answer