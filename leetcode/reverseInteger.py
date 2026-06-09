class Solution:
    def myAtoi(self, s: str) -> int:
        def check(x):
            if (x > 2**31 - 1):
                return 2**31 - 1
            elif (x < -2**31):
                return -2**31
            else:
                return x
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
                  return check(int(answer) * (-1)**signed )
            answer += editS[i] 
            print(answer)
        if (answer == ''):
            return 0
        return check(int(answer) * (-1)**signed)