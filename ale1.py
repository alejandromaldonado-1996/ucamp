# se uso def para crear una funcion (bloque) y llamar(reintntar) el codigo 
def calculadora():
#try es la funcion que nos ayudara a marcar el rango del codigo donde se colocaran las excepciones, para que la aplicion no se bloquee
    try:
        #se agrego \n para colocar calculadora de masa corporal en nueva linea 
        print("Servicio Médico  \nCalculadora de Masa Corporal")
        
        nombre = str(input("Ingresa tu nombre:  "))
        apellido_paterno  = str(input("Ingresa tu apellido paterno:  "))
        apellido_materno= str(input("ingresa tu apellido materno: "))
        edad= input("Cual es tu edad:  ")
        nombre_completo = nombre + " " + apellido_paterno + " " + apellido_materno
        
        #se concatena hola mas la variable nombre completo con el resto de la oracion.
        print("Hola " + nombre_completo + ", Iniciemos.")
# se coloca float antes del input para  que el volor que ingrese, se convierta en un numero flotante
        peso = float(input("Ingresa tu peso en kg: "))
        print(nombre + ", Tu peso es  de " + str(peso) + " kg.")

        estatura = float(input("Para continuar, ingresa tu estatura en metros: "))

        imc = peso / estatura**2
        

        # round redondea a dos caracteres el IMC para no presentar mas valores, despues del punto
# se agrega str antes de IMC para cuando lo imprima lo coloque como un string
        print("Tu índice de masa corporal (IMC) es: " + str(round( imc , 2)))
        # if es la funcion que evalua en este caso si el imc es menor o igual al valor asignado
        if imc < 18.5:
            print("La clasificacion de tu peso es: \nBajo peso")

        #elif es la funcion que continua con el codigo si el valor de if es diferente , se pueden colocar los elif que se requieran.
        elif 18.5 <= imc < 25:
            print ("La clasificacion de tu peso es: \n Peso normal")
        elif 25 <= imc < 30:
            print("La clasificacion de tu peso es: \n Sobrepeso")
        elif 30 <= imc < 35:
            print("La clasificacion de tu peso es: \n  Obesidad grado 1")
        elif 35 <= imc < 40:
            print("La clasificacion de tu peso es: \n  Obesidad grado 2")
        elif imc >= 40.00:
            print("La clasificacion de tu peso es: \n  Obesidad grado 3 (mórbida)")
        # else es la funcion que termina el codigo si ninguna de las opciones son las 
        else:"Intente de nuevo"

        
#except se coloca al final del rango de el codigo donde 
#ValueError: captura errores si el usuario escribe letras u otros caracteres inválidos.
    except ValueError:
        print(" Error: Debes ingresar números válidos para peso y estatura.")
        calculadora()  # Vuelve a intentar

#ZeroDivisionError: por si alguien pone 0 como estatura.
    except ZeroDivisionError:
        print(" Error: La estatura no puede ser cero.")
        calculadora()  # Vuelve a intentar
# (llama) reinicia la aplicacion 
calculadora()
print("\nGracias por usar la calculadora de IMC. ")
print("\n\n\n\nProyecto 1 Alejandro Maldonado Ponce.")



