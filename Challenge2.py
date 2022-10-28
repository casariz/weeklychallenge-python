# /*
#  * Reto #2
#  * LA SUCESIÓN DE FIBONACCI
#  * Fecha publicación enunciado: 10/01/22
#  * Fecha publicación resolución: 17/01/22
#  * Dificultad: DIFÍCIL
#  *
#  * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
#  * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
#  * 0, 1, 1, 2, 3, 5, 8, 13...
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

#Solución dada por Casariz (Daniel Casallas)

n =0
primerNum = 0
segundoNum = 1
contador = 0
print(primerNum)
print(segundoNum)
while n <= 23:
    contador = primerNum + segundoNum
    segundoNum = segundoNum+ contador
    primerNum = contador

    if primerNum < segundoNum:
        print(primerNum)
        print(segundoNum)
    elif primerNum > segundoNum:
           print(segundoNum)
           print(primerNum)
    else: print(primerNum)
    n+=1
    
