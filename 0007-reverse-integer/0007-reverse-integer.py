class Solution:
    def reverse(self, x: int) -> int:
        def check(x):
            if (x > 2**31 - 1 or x < -2**31):
                return 0
            else:
                return x
        if (x >= 0):
            xString = str(x)
            newX = xString[::-1]
            return check(int(newX))
        else:
            xString = str(x)[1:]
            newX = xString[::-1]
            return check(-int(newX))
