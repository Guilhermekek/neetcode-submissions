class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cont_s = Counter(s)
        cont_t = Counter(t)
        return cont_s == cont_t

        