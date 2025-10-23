print("1. Contador con blucle while")
print("2. Imprimir nuémeros pares con bucle for")
print("3. Contar los dígitos de un número")
print("4. Calcular la suma de los número enteros")
print("5. Conteo descendente")
print("6. Imprimir la tabla de multiplicar de un número")
print("7. Imprimir números impares hasta un número dado")
print("8. Imprimir la serie de Fibonacci")
print("9. Calcular el factorial de un número")
print("10. Comprobación de contraseña")
print("11. Salir")

#Solicitud de órden

opcion = int(input("Seleccione una opción (1-11): "))

#Volver a pedir la órden si es incorrecta
while opcion < 1 or opcion > 11:
    print("Error: El número de órden es incorrecto.")
    opcion = int(input("Seleccione una opción (1-11): "))

#Condiciones
if opcion == 1:
#COntados con bucle while
    ingresar_valor = int(input("Ingrese un número entero positivo: "))
    n = 1
    while n <= ingresar_valor:
        print(n)
        n += 1

#Imprimir números pares con bucle for
elif opcion == 2:
    #pedir valor
    ingresar_valor = int(input("Ingrese un número entero positivo: "))
    #bucle for
    for n in range(1, ingresar_valor + 1):
        if n % 2 == 0:
            print(n)

#Contar los dígitos de un número
elif opcion == 3:
#Pedir valor
    ingresar_valor = int(input("Ingrese un número entero positivo: "))
    contador = 0
#Condicionales
    if ingresar_valor == 0:
        contador = 1
    else:
        while ingresar_valor > 0:
            ingresar_valor = ingresar_valor // 10
            contador += 1
    print(f"El número ingresado tiene {contador} dígitos.")

#Calcular la suma de los número enteros
elif opcion == 4:
    suma = 0
    for n in range(1, 101):
        suma += n
#Mostrar el resultado
    print(f"La suma de los número enteros del 1 al 100 es: {suma}")

#Conteo descendente
elif opcion == 5:
    #Pedir valor
    ingresar_valor = int(input("Ingrese un número entero positivo: "))
    #Bucle
    while ingresar_valor >= 0:
        print(ingresar_valor)
        ingresar_valor -= 1

#Imprimir la tabla de multiplicar de un número
elif opcion == 6:
#pedir valor
    ingresar_valor = int(input("Ingresar el número de tabla a multiplicar: "))
    #Bucle
    for n in range(1, 11):
        resultado = ingresar_valor * n
        print(f"{ingresar_valor} x {n} = {resultado}")

#Imprimir números impares hasta un número dado
elif opcion == 7:
    #Pedir valor hasta que sea positivo
    ingresar_valor = int(input("Ingrese un número entero positivo: "))
    while ingresar_valor <= 0:
        print("Error: Debe ingresar un número entero positivo.")
        ingresar_valor = int(input("Ingrese un número entero positivo: "))

    #Imprimir números impares
    contador = 1
    print(f"Números impares desde 1 hasta {ingresar_valor}:")
    while contador <= ingresar_valor:
        print(contador)
        contador += 2

#Imprimir la serie de Fibonacci
elif opcion == 8:
    #Pedir valor
    ingresar_valor = int(input("Ingresar el número de términos de la serie: "))
    v1, v2 = 0, 1
    print("Serie de Fibonacci:")
    for n in range(ingresar_valor):
        print(v1, end=" ")
        v1, v2 = v2, v1 + v2

#Calcular el factorial de un número
elif opcion == 9:
    #Pedir valor
    ingresar_valor = float(input("Ingrese un número: "))
    factorial = 1
    contador = 1
    #Bucle
    while contador <= ingresar_valor:
        factorial *= contador
        contador += 1
        print(f"El factorial de {ingresar_valor} es: {factorial}")

#Comprobación de contraseña
elif opcion == 10:
    usuario_real = "Alvi"
    contrasena_real = "Alvi102023"
    #bucle
    while True:
        ingresar_usuario = input("Ingrese su nombre de usuario: ")
        ingresar_contrasena = input("Ingrese la contraseña: ")       
        if ingresar_usuario == usuario_real and ingresar_contrasena == contrasena_real:
            print(f"¡Acceso concedido! Bienvenido, {usuario_real}.")
            break
        else:
            print("Error: Al parecer el nombre de usuario o contraseña son incorrectos. Intente de nuevo.")
#Salir
else:
    print("Saliendo del programa. ¡Gracias por usar el programa!")
    



