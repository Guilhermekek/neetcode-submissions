class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valores = {} # crio um dicionario
        for index,num in enumerate(nums): # me da o index + numero
            complemento = target - num # valor que preciso
            if complemento in valores: # se o valor que preciso esta dentro de valores
                return [valores[complemento],index] 
            valores[num] = index 
            
            

        