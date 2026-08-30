from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=list(Counter(tasks).values())
        m=max(freq)
        cnt=freq.count(m)
        return max(len(tasks),(m-1)*(n+1)+cnt)