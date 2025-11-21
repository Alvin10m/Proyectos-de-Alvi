#Menú de opciones

print("1. Determinar si un número es positivo, negativo o cero")
print("2. Número par o impar")
print("3. Determinas si es mayor de edad")
print("4. Determinas si un número es multiplo de 5")
print("5. Descuento por edad")
print("6. Calificción aprobatoria")
print("7. Detnerminar día de la semana correrpondiente")
print("8. Determinar si un número es mayor que otro")
print("9. Determinar entre 3 números cual es el mayor")
print("10. Clasificación de ángulos")
print("11. Calcular impuesto")
print("12. Clasificación de números")
print("13. Verificación de año bisiesto")
print("14. Conversión de calificaciones")
print("15. Comparar tres longitudes")
print("16. Calcular descuento")
print("17. Determinar el dipo de un triángulo")
print("18. Evaluar temperatura") 
print("19. Conversión de horas a turnos")
print("20. Clasificar IMC")
print("0. Salir")
    # Selección de opción

opcion = int(input("Seleccione una opción del 0 al 20: "))
       
if opcion == 0:
        print("Gracias por utilizar el programa.")  



#Solicite un número al usuario y determine si es positivo,
#negativo o cero.
if opcion == 1:
    numero = float(input("Ingrese un número: "))
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else: 
        print("El número es cero.")
#Pide al usuario que ingrese un número entero y determina si es par o impar.
elif opcion == 2:
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        print("El número es par.")
    else: 
        print("El número es impar.")
#Determinar si una persona es mayor de edad
elif opcion == 3:
    persona = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print(f"{persona} es mayor de edad")
    else:
        print(f"{persona} es menor de edad.")
#Determinar si un número es múltiplo de 5
elif opcion == 4:
    numero = int(input("Ingrese un numero: "))
    if numero % 5 == 0:
        print(f"El número {numero} es múltiplo de 5.")
    else: 
        print(f"El número {numero} no es múltiplo de 5.")
#Calcular descuento por edad
elif opcion == 5:
    edad = int(input("Ingrese la edad del cliente: "))
    precio = float(input("Ingrese el pecio de la taquilla: "))
    if edad >= 60:
        descuento = precio * 0.25
        precio_final = precio - descuento
        print(f"El precio con descuento es: {precio_final}")
#Calificación aprobatoria
elif opcion == 6:
    calificacion = float(input("Ingrese la calificación obtenida: "))
    if calificacion >= 60:
        print("Aprobado")
    else:
        print("Reprobado")
#Determinar día de la semana correspondiente
elif opcion == 7:
    numero_de_dia = int(input("Ingrese un número del 1 al 7: "))
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    print(dias.get(numero_de_dia, "Número inválido"))
#Determinar si un número es mayor que otro
elif opcion == 8:
    primer_valor = float(input("Ingrese el primer número: "))
    segundo_valor = float(input("Ingrese el segundo número: "))
    if primer_valor > segundo_valor:
        print(f"El número {primer_valor} es mayor que {segundo_valor}.")
    elif primer_valor < segundo_valor:
        print(f"El número {segundo_valor} es mayor que {primer_valor}.")
    else:
        print("Los dos números ingresados son iguales")
#Determinar entre 3 números cual es el mayor
elif opcion == 9:
    primer_valor = float(input("Ingrese el primer número: "))
    segundo_valor = float(input("Ingrese el segundo número: "))
    tercer_valor = float(input("Ingrese el tercer número: "))
#Comparar los números
    if primer_valor > segundo_valor and primer_valor > tercer_valor:
        print(f"El número mayor es: {primer_valor}")
    elif segundo_valor > primer_valor and segundo_valor > tercer_valor:
        print(f"El número mayor es: {segundo_valor}")
    elif tercer_valor > primer_valor and tercer_valor > segundo_valor:
        print(f"El número mayor es: {tercer_valor}")
    else: 
        print("Entre los números ingresados hay números iguales")
#Clasificación de ángulos
#Medida del ángulo
elif opcion == 10:
    grado_del_angulo = float(input("Ingrese la medida del ángulo en grados: "))
#clasificación 
    if grado_del_angulo < 90:
        print("La medida corresponde a un ángulo agudo.")
    elif grado_del_angulo == 90:
        print("La medida corresponde a un ángulo recto.")
    elif grado_del_angulo > 90 and grado_del_angulo < 180:
        print("La medida corresponde a un ángulo obtuso.")
    elif grado_del_angulo == 180:
        print("La medida corresponde a un ángulo llano.")
    else:
        print("La medida ingresada no corresponde a ningún ángulo válido, por favor ingrese un valor válido.")
#Calcular impuesto
elif opcion == 11:
    # Pedimos el salario
    pedir_salario = float(input("Ingrese su salario mensual: "))

    # Damos las condiciones
    if pedir_salario < 10000:
        descuento = 0
        print("Tu salario no aplica para impuesto.")
    elif pedir_salario >= 10000 and pedir_salario <= 30000:
        descuento = pedir_salario * 0.10
        print("El descuento por impuesto es del 10%.")
    else:
        descuento = pedir_salario * 0.20
        print("El descuento de acuerdo a su salario es del 20%.")

    # Calculamos el salario total (se hace siempre)
    salario_total = pedir_salario - descuento

    # Damos el resultado
    print(f"El impuesto aplicado a su salario es de: {descuento:.2f}, y su salario total es de: {salario_total:.2f}")

    #Clasificación de números
elif opcion == 12:
    valor1 = float(input("Ingrese el primer número: "))
    valor2 = float(input("Ingrese el segundo número: "))
    valor3 = float(input("Ingrese el tercer número: "))
    #Condicionales
    if valor1 > 0 and valor2 > 0 and valor3 > 0:
        print("Los tres valores son positivos.")
    elif valor1 < 0 and valor2 < 0 and valor3 < 0:
        print("Los tres valores son negativos.")
    elif valor1 == 0 and valor2 == 0 and valor3 == 0:
        print("Los tres valores son cero.")
    else:
        print("Los valores son mixtos")
#Verificación de año bisiesto
elif opcion == 13:
# solicitar año
    solicitar_año = int(input("Ingrese un año para la verificación: "))
    #verificación
    if (solicitar_año % 4 == 0 and solicitar_año % 100 != 0 or solicitar_año % 400 == 0):
        print(f"El año {solicitar_año} es bisiesto.")
    else:
        print(f"El año {solicitar_año} no es bisiesto.")

#Conversión de calificaciones
elif opcion == 14:
    calificacion = float(input("Ingrese la calificación del 0 al 100: "))
    #mostramos error si la calificación no cumple el rango
    while calificacion < 0 or calificacion > 100:
        print("Error: la calificación debe estar entre 0 y 100.")
    #Volver a pedir la calificación
        calificacion = float(input("Ingrese la calificación del 0 al 100: "))
    #codicionales
    if calificacion >= 90 and calificacion <= 100:
        print("La calificación es A.")
    elif calificacion >= 80 and calificacion < 89:
        print("La calificación es B.")
    elif calificacion >= 70 and calificacion < 79:
        print("La calificación es C.")
    elif calificacion >= 60 and calificacion < 69:
        print("La calificación es D.")
    else: 
        print("La calificación es F.")

#Comparar tres longitudes
elif opcion == 15:
    #Solicitar longitudes
    v1 = float(input("Ingrese la primera longitud: "))
    v2 = float(input("Ingrese la segunda longitud: "))
    v3 = float(input("Ingrese la tercera longitud: "))
    #Condicionales
    if (v1 + v2 > v3) and (v1 + v3 > v2) and (v2 + v3 > v1):
        print("Las longitudes ingresadas pueden formar un triángulo.")
    else:
        print("Las longitudes ingresadas no pueden formar un triángulo.")

#Calcular descuento
elif opcion == 16:
    #Pedir precio del producto
    precio_producto = float(input("Ingrese el precio del producto: "))
    
    #Condicionales  
    if precio_producto < 50:
        descuento = 0.0
        print("A su compra no le aplica descuento.")
    elif precio_producto >= 50 and precio_producto <= 100:
        descuento = precio_producto * 0.05
        precio_total = precio_producto - descuento
        print(f"El descuento aplicado es del 5% y el precio a pagar es: {precio_total:.2f}")
    else:
        descuento = precio_producto * 0.10
        precio_total = precio_producto - descuento
        print(f"El descuento aplicado es del 10% y el precio a pagar es: {precio_total:.2f}")

#Determinar el tipo de un triángulo
elif opcion == 17:
    #Solicitar lados del triángulo
    lad1 = float(input("Ingrese la longitud del primer lado: "))
    lad2 = float(input("Ingrese la longitud del segundo lado: "))
    lad3 = float(input("Ingrese la longitud del tercer lado: "))
    #Condicionales
    if lad1 == lad2 and lad2 == lad3:
        print("Los datos corresponden a un triángulo equilátero.")
    elif lad1 == lad2 or lad1 == lad3 or lad2 == lad3:
        print("Los datos corresponden a un triángulo isósceles.")
    else: 
        print("Los datos corresponden a un triángulo escaleno.")

#Evaluación de temperatura 
elif opcion == 18:
    #pedimos temperatura
    pedir_temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
    #condicionale
    if pedir_temperatura < 0:
     print("Hace mucho frío, es recomendable utilizar ropa cálida")
    elif pedir_temperatura >= 0 and pedir_temperatura <= 20:
     print("El clima está fresco")
    elif pedir_temperatura >= 21 and pedir_temperatura <= 30:
     print("El clima es agradable")
    else:
     print("Hace bastante calor. Es recomendable estar en lugares frescos y en caso de salida utilizar protector solar y ropa ligera ")

#Conversión de horas a turnos
elif opcion == 19:
    #solicitar hora
    solicitar_hora = int(input("Ingrese la hora de 0 a 23: "))
    #Vol ver a pedir la hora si no está en el rango
    while solicitar_hora < 0 or solicitar_hora > 23:
        print("Error: la hora ingresada no está en el rango definido.")
        solicitar_hora = int(input("Ingrese la hora de 0 a 23: "))
    #Condicionales
    if solicitar_hora >= 6 and solicitar_hora <= 11:
        print("La hora ingresada corresponde al turno de la Mañana.")
    elif solicitar_hora >= 12 and solicitar_hora <= 17:
        print("La hora ingresada corresponde al turno de la Tarde.")
    elif solicitar_hora >= 18 and solicitar_hora <= 23:
        print("La hora ingresada corresponde al turno de la Noche.")
    else:
        print("La hora ingresada corresponde al turno de la Madrugada.")
    
#Clasificar IMC
elif opcion == 20:
    #Solicitar peso y altura
    solicitar_peso = float(input("Ingrese su peso en kilogramnos: "))
    solicitar_altura = float(input("Ingrese su altura en metros: "))
    #Calcular IMC
    resultado_de_IMC = solicitar_peso / (solicitar_altura ** 2)
    #Condicionales
    if resultado_de_IMC < 18.5:
        print("Tiene bajo peso, es recomendiable que visite un especialista.")
    elif resultado_de_IMC >= 18.5 and resultado_de_IMC < 24.9:
        print("Tiene un peso normal")
    elif resultado_de_IMC >= 25 and resultado_de_IMC < 29.9:
        print("Tiene sobrepeso, es recomendable que cuide su alimentación")
    else:
        print("Tiene obesidad, es recomendable que visite un especialista.")



