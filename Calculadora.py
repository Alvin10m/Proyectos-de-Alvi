#Calculadora de Numeros: Crea un programa 
#que permita realizar diversas operaciones con dos 
#numero que se introducen por el teclado.Multiplicado, 
#división, suma, resta, modulo o resto, raiz cuadrada y potencia

import math

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Modulo o Resto")
print("6. Raiz Cuadrada")
print("7. Potencia")

operacion = int(input("Por favor, elige el tipo de operación (1-7): "))

primer_valor  = float(input("Introduzca el primer valor: "))
segundo_valor = float(input("Intoduzca el segundo valor: "))

if operacion == 1:
    print(f"La suma de {primer_valor} + {segundo_valor} es: {primer_valor + segundo_valor}")
elif operacion == 2:
    print(f"La resta de {primer_valor} - {segundo_valor} es: {primer_valor - segundo_valor}")
elif operacion == 3:
    print(f"La multiplicación de {primer_valor} * {segundo_valor} es: {primer_valor * segundo_valor}")
elif operacion == 4:
    print(f"La división de {primer_valor} / {segundo_valor} es: {primer_valor / segundo_valor}")
elif operacion == 5: 
    print(f"El módulo o resto de {primer_valor} % {segundo_valor} es: {primer_valor % segundo_valor}")
elif operacion == 6:
    print(f"La raíz cuadrada de {primer_valor} es: {math.sqrt(primer_valor)}")
elif operacion == 7:
    print(f"{primer_valor} elevado a la {segundo_valor} es: {primer_valor ** segundo_valor}") 
else:
    print("El tipo de operación no está disponible en estos momentos")
        