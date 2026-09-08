class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        o="O"
        r=len(board)
        c=len(board[0])
        q=deque()
        for i in range(r):
            if board[i][0]==o:
                q.append((i,0))
            if board[i][c-1]==o:
                q.append((i,c-1))
        for j in range(c):
            if board[0][j]==o:
                q.append((0,j))
            if board[r-1][j]==o:
                q.append((r-1,j))
        while q:
            i,j=q.popleft()
            board[i][j]="#"
            for di,dj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if not((0<=di<r) and (0<=dj<c)):
                    continue
                if board[di][dj]!=o:
                    continue
                q.append((di,dj))
                board[di][dj]="#"
        for i in range(r):
            for j in range(c):
                if board[i][j]==o:
                    board[i][j]="X"
                elif board[i][j]=="#":
                    board[i][j]=o