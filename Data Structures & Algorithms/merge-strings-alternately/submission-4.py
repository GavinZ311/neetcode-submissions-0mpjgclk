class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first = second = 0
        # new_string = ""
        #Try to use a StringBuilder, list of characters to make this more efficient
        #since you are creating a new string in the loop each time it adds
        res = []

        #Just use and to not overcomplicate this

        while first < len(word1) and second < len(word2):
            # if first >= len(word1):
            #     new_string += word2[first::]
            #     break
            # elif second >= len(word2):
            #     new_string += word1[second::]
            #     break
            #Overcomplicating and brute forcing

            # new_string += word1[first]
            # new_string += word2[second]
            res.append(word1[first])
            res.append(word2[second])
            first += 1
            second += 1
        #Just add it anyway, when the other one reached the end    
        res.append(word1[first:])
        res.append(word2[second:])
        
        return "".join(res)
        
