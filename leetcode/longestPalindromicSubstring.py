class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1: r]
        answer = ""
        for i in range(len(s)):
            #짝수일 경우
            even = palindrome(i, i+1)
            #홀수일 경우
            odd = palindrome(i, i)
            if (len(even) > len(answer)):
                answer = even
            if (len(odd) > len(answer)):
                answer = odd
        return answer
