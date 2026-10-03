class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cont_s,cont_t = {},{}
        for letra in s:
            cont_s[letra] = cont_s.get(letra, 0) + 1
        for letra in t:
            cont_t[letra] = cont_t.get(letra, 0) + 1
        return cont_s == cont_t
        