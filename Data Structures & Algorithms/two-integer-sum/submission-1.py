class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valores = {} # crio um dicionario para armazenar o valor e o index
        for index, num in enumerate(nums):# uso enumerate para me dar tanto o valor quanto o index
            complemento = target - num # o valor que preciso, esse valor vai se atualizar a cada loop com base no num fornecido no loop
            if complemento in valores:#se o valor existir no nosso dicionario
                return[valores[complemento],index]
            valores[num] = index 
        