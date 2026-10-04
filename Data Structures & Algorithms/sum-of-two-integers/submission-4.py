class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF          # 32 bits todos em 1
        MAX = 0x7FFFFFFF           # maior positivo em 32 bits
        while b != 0:
            vai_um = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = vai_um
        return a if a <= MAX else ~(a ^ MASK)