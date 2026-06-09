class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = ""
        if numRows == 1:
            answer = s
            return answer
        elif numRows == 2:
            for i in range(0, len(s), 2):
                answer += s[i]
            for j in range(1, len(s), 2):
                answer+=s[j]
            return answer
        else:
            cycle = 2*numRows-2
            for i in range(numRows):
                for j in range(i, len(s), cycle):
                    answer += s[j]
                    if i != 0 and i != numRows-1 and j+cycle-2*i < len(s):
                        answer += s[j+cycle-2*i]
                
            return answer
