class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        hash=Counter(tiles)
        def bt():
            tiles=0
            for ch in hash:
                if hash[ch]:
                    hash[ch]-=1
                    tiles+=bt()+1
                    hash[ch]+=1
            return tiles
        return bt()
