class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        # goal is to make s a prefix by using up entire word in words..
        # not just comparing lengths
        temp = ""
        for w in words:
            temp += w
            if s == temp:
                return True
            if len(temp)>len(s):
                break
        return False
