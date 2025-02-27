class ProductOfNumbers:

    def __init__(self):
        self.prod=[1]

    def add(self, num: int) -> None:
        if num:
            self.prod.append(self.prod[-1]*num)
        else:
            self.prod=[1]

    def getProduct(self, k: int) -> int:
        # print(self.prod)
        if k>len(self.prod)-1:
            return 0
        return self.prod[-1]//self.prod[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
