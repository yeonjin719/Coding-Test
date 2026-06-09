class Solution:
    def myAtoi(self, s: str) -> int:
        editS = s.strip().split(" ")[0]
        signed = 0
        answer = ''
        for i in range(len(editS)):
            print(editS[i])
            if i == 0:
                if (editS[i] == '-'):
                    signed = 1
                    continue
                elif (editS[i] == '+'):
                    signed = 0
                    continue
            if (editS[i].isnumeric() == False):
                if (answer == ''):
                    return 0
                else: 
                  return int(answer) * (-1)**signed 
            answer += editS[i] 
            print(answer)
        return int(answer) * (-1)**signed

# Example usage:
solution = Solution()
print(solution.myAtoi("words and 987")) # Output: 0