class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_idx = s_idx = 0
        count = 0
        s.sort()
        g.sort()

        while g_idx < len(g) and s_idx < len(s):
            if s[s_idx] >= g[g_idx]:
                count += 1
                g_idx += 1
            s_idx += 1
            
        return count
