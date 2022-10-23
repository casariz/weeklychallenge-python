# /*
#  * Reto #1
#  * ¿ES UN ANAGRAMA?
#  * Fecha publicación enunciado: 03/01/22
#  * Fecha publicación resolución: 10/01/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
#  * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#  * NO hace falta comprobar que ambas palabras existan.
#  * Dos palabras exactamente iguales no son anagrama.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

#solucion dada por Casariz (Daniel Casallas)
#Día: 23/10/2022
def isAnagram(word1:str, word2:str):

    bandera = True
    anagram1 = list(word1)
    anagram2 = list(reversed(word2))
    if (anagram1 != anagram2):
        bandera = False
    else: 
        bandera = True

    return bandera


firtWord = input("Ingrese la primera palabra: ")
secondWord = input("Ingrese la segunda palabra: ")

result = isAnagram(word1 = firtWord, word2 = secondWord)

print("¿Son un anagrama?: ", result)
