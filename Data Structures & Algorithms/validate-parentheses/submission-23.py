class Solution:
    def isValid(self, s: str) -> bool:
        op = ["{","(","["]
        cl = ["}",")","]"]
        word = []
        stackCL = []

        if len(s)<=1:
            return False
            
        for i in s:
            word.append(i)

        for w in range(len(word)):
            for i in range(len(op)):
                if word[w] == op[i]:
                    stackCL.append(cl[i])
                elif word[w] == cl[i]:
                    if stackCL:
                        if stackCL[-1] == cl[i]:
                            stackCL.pop()
                        else:
                            return False
                    else:
                        return False

        if not stackCL:
            return True
        return False

        