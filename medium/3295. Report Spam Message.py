class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedWords=set(bannedWords)
        ans=0
        # message=set(message)
        for i in message:
            if i in bannedWords:
                ans+=1
                if ans==2:
                    return True
        return False
