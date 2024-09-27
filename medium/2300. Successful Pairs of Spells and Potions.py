class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sortedPotions = sorted(potions)
        n = len(potions)
        result = []
        def binS(spell, success):
            low, high = 0, n - 1
            min_potion_strength = (success + spell - 1) // spell
            while low <= high:
                mid = (low + high) // 2
                if sortedPotions[mid] < min_potion_strength:
                    low = mid + 1
                else:
                    high = mid - 1
            return low
        for spell in spells:
            idx = binS(spell, success)
            result.append(n - idx)
        return result
