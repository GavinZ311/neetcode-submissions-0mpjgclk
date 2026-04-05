class Solution:
    def isValid(self, s: str) -> bool:
        openStack = ['(', '{', '[']
        closeStack = [')', '}', ']']
        stack = []
        word = []

        for st in s:
            word.append(st)

        for w in range(len(word)):
            for i in range (len(openStack)):
                if word[w] == openStack[i]:
                    stack.append(closeStack[i])
                elif word[w] == closeStack[i]:
                    if stack:
                        if stack[-1] != word[w]:
                            return False
                        else:
                            stack.pop()
                    else:
                        return False
        
        if not stack:
            return True
        else:
            return False