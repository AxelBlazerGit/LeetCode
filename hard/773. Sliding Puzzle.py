class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {
            0: [1, 3], 
            1: [0, 2, 4], 
            2: [1, 5], 
            3: [0, 4], 
            4: [1, 3, 5], 
            5: [2, 4]
        }
        cur = [x for i in board for x in i]
        dq = deque([(cur, 0)]) # state,moves
        hash = set([tuple(cur)])
        while dq:
            state,cur=dq.popleft()
            if state==[1,2,3,4,5,0]:
                return cur
            idx=state.index(0)
            for move in moves[idx]:
                temp=state[:]
                temp[move],temp[idx]=temp[idx],temp[move]
                if tuple(temp) not in hash:
                    hash.add(tuple(temp))
                    dq.append((temp,cur+1))
        return -1
