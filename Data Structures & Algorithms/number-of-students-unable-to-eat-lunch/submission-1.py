from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = deque(students)
        sa = deque(sandwiches)
        i = len(st)

        while i > 0 and st:
            if st[0] == sa[0]:
                st.popleft()
                sa.popleft()
                i = len(st)
            else:
                st.append(st.popleft())
                i -= 1

        return len(st)
                
        

