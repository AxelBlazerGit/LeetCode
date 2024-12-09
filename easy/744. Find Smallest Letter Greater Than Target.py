class Solution:
    def ascii(self,x):
        return ord(x)-97
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters=[self.ascii(i) for i in letters]
        target=self.ascii(target)

        def binS(arr, target):
            low, high = 0, len(arr) - 1
            result = -1

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] > target:
                    result = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return result
        
        check=binS(letters,target)

        return chr(97+letters[check]) if check!=-1 else chr(97+letters[0])
