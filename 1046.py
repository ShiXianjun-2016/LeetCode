class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if stones.length == 0:
            return 0
        if stones.length == 1:
            return stones[0]
        
        stones.sort()
        
        if stones[-1] == stones[-2]:
            del stones[-2:]
            return self.lastStoneWeight(self, stones)
        
        if stones[-1] != stones[-2]:
            int newStone = stones[-1] - stones[-2]
            del stones[-1]
            stones[-1] = newStone
            return self.lastStoneWeight(self, stones)

