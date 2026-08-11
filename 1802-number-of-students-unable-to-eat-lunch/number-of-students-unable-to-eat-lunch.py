class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q=deque(students)
        i=0
        count=0
        while q and count<len(q):
            if q[0]==sandwiches[i]:
                q.popleft()
                i+=1
                count=0
            else:
                q.append(q.popleft())
                count+=1
        return len(q)