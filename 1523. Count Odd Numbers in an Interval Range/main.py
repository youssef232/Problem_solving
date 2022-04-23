class Solution:
    def countOdds(self, low: int, high: int) -> int:
        def countOdds2(num):
            if num % 2:
                return int(num // 2 + 1)
            else:
                return int(num / 2)

        if (low % 2 == 0 and high % 2 == 0) or (low % 2 == 0 and high % 2):
            return countOdds2(high) - countOdds2(low)
        else:
            return countOdds2(high) - countOdds2(low) + 1

