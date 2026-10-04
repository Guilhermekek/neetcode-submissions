class Solution:
    def _contar(self, texto):
        cont = {}
        for letra in texto:
            cont[letra] = cont.get(letra, 0) + 1
        return cont

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self._contar(s) == self._contar(t)