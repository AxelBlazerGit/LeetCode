class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors)<3:
            return False
        movesA,movesB=0,0
        astreak,bstreak=0,0
        for i in range(len(colors)):
            if colors[i]=='B':
                if bstreak==0:
                    bstreak=1
                else:
                    bstreak+=1
                
                movesA+=astreak-2 if astreak>=3 else 0
                astreak=0
            else:
                if astreak==0:
                    astreak=1
                else:
                    astreak+=1
                
                movesB+=bstreak-2 if bstreak>=3 else 0
                bstreak=0
        if bstreak:
            movesB+=bstreak-2 if bstreak>=3 else 0
        else:
            movesA+=astreak-2 if astreak>=3 else 0
        if movesA>movesB:
            return True
        else:
            return False


            
