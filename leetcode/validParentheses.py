class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for i in range(len(s)):
            if (s[i] == '(' or s[i]=='{' or s[i] == '['):
                queue.append(s[i])
            else:
                if (s[i] == ')'):
                    if (len(queue) == 0 or queue[-1] != '('):
                        return False
                    del queue[-1]
                elif (s[i] == '}'):
                    if (len(queue) == 0 or queue[-1] != '{'):
                        return False
                    del queue[-1]
                elif (s[i] == ']'):
                    if (len(queue) == 0 or queue[-1] != '['):
                        return False
                    del queue[-1]
                else:
                    return False
        if len(queue) == 0:
            return True
        else:
            return False                    