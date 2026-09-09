class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w_idx = a_idx = 0

        while w_idx < len(word) and a_idx < len(abbr):
            #num = "0"
            if abbr[a_idx] == '0':
                return False
            
            # while abbr[a_idx].isdigit():
            #     num += abbr[a_idx]
            #     a_idx += 1
            #     if num == "0":
            #         return False
            if word[w_idx] == abbr[a_idx]:
                w_idx, a_idx = w_idx+1, a_idx+1
            #If one does not equal and abbr is all characters -> False
            elif abbr[a_idx].isalpha():
                return False
            else:
                subLen = 0
                while a_idx < len(abbr) and abbr[a_idx].isdigit():
                    subLen = subLen * 10 + int(abbr[a_idx])
                    a_idx += 1
                w_idx += subLen
        
        return w_idx == len(word) and a_idx == len(abbr)

            
            # while w_idx < int(num):
            #     w_idx += 1
            
            # if w_idx >= len(word):
            #     return False
            # elif abbr[a_idx] != word[w_idx]:
            #     return False
            # else:
            #     w_idx += 1
            #     a_idx += 1

        # return True
            

            


