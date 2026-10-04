class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ranqueado = Counter(nums)
        ranqueados = list(ranqueado.keys())
        ranqueados.sort(key=lambda x: -ranqueado[x])
        return ranqueados[:k]

