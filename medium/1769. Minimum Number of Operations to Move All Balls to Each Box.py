class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ops = [0] * len(boxes)

        b, m = 0, 0
        for i in range(len(boxes)):
            m += b 
            ops[i] += m
            b += int(boxes[i])
        
        b, m = 0, 0
        for i in range(len(boxes) - 1, -1, -1):
            m += b
            ops[i] += m
            b += int(boxes[i])
        return ops
