class Solution:
    def intToRoman(self, num: int) -> str:
        numRoman = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1:'I'}
        nums = [1000, 500, 100, 50, 10, 5, 1]
        answer = ""
        thousandNum = (num // 1000)*1000
        hundredNum = ((num - thousandNum) // 100) * 100
        tenNum = ((num - thousandNum - hundredNum) // 10) * 10
        oneNum = num - thousandNum - hundredNum - tenNum
        
        for i in ([thousandNum, hundredNum, tenNum, oneNum]):
            if (str(i)[0] == '4'):
                answer += numRoman[int('1'+((len(str(i))) - 1)*'0')]
                answer += numRoman[int('5'+((len(str(i))) - 1)*'0')]
            elif (str(i)[0] == '9'):
                answer += numRoman[int('1'+((len(str(i))) - 1)*'0')]
                answer += numRoman[int('1'+(len(str(i)) * '0'))]
            else:
                for j in nums:
                    while (i >= j):
                        cnt = i // j
                        answer += (numRoman[j]*cnt)
                        i -= cnt * j
        return answer