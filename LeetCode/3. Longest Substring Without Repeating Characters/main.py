class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength
    
# Crear una instancia de la clase Solution
sol = Solution()

# Obtener el input del usuario
s = input("Ingresa una cadena: ")

# Llamar al método lengthOfLongestSubstring con el input
ans = sol.lengthOfLongestSubstring(s)

# Imprimir la respuesta
print("La longitud de la subcadena más larga sin caracteres repetidos es:", ans)
