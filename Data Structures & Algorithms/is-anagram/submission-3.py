class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # s_list = list(s)
        # t_list = list(t)
        # s_list.sort()
        # t_list.sort()


        # for i in range(len(s_list)):
        #     if s_list[i] != t_list[i]:
        #         return False

        # return True


#Now, how to do this in the dictionary way?
        s_count, t_count = {}, {}

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) +1
            t_count[t[i]] = t_count.get(t[i], 0) +1

        for k in s_count:
            if s_count[k] != t_count.get(k, 0):
                return False

        return True
