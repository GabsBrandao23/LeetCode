class Solution(object):  
    def isPalindrome(self, x):  
        """
        :type x: int
        :rtype: bool
        """
        number = x       # Armazena o valor original de x para comparar no final
        _reversed = 0    # Variável que vai acumular o número de x ao contrário

        if (x < 0):      # Números negativos NUNCA são palíndromos (ex: -121 -> 121-)
            return False  # Retorna False e encerra a função

        while (x > 0):                        # Enquanto x for maior que 0
            figure = x % 10                   # Extrai o último dígito de x com sobra da divisão
            _reversed = (_reversed * 10) + figure  # Move os dígitos coletados uma casa pra left e add o novo dígito
            x = x // 10                       # Remove o último dígito de x 

        return _reversed == number  # Retorna True se o número invertido for igual ao original

numero = int(input("Digite um número: "))  # Lê o input e converte para inteiro
sol = Solution()                           # Cria uma instância da classe
resultado = sol.isPalindrome(numero)       # Chama o método com o número digitado
print(resultado) 