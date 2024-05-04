class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed = []
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                compressed.append(chars[i - 1])
                if count > 1:
                    compressed.extend(str(count))
                count = 1
        #managing last char 
        compressed.append(chars[-1])
        if count > 1:
            compressed.extend(str(count))
        
        chars.clear()
        chars.extend(compressed)
        
        return len(chars)



























# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         # return len(chars)
#         freq={}
#         for i in chars:
#             if i in freq:
#                 continue
#             else:
#                 freq[i]=chars.count(i)
#         chars.clear()
#         for i in freq:
#             chars.append(i)
#             if freq[i]!=1:
#                 chars.extend(str(freq[i]))
#         return len(chars)
            
