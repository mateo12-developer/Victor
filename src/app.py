
# Aquí empieza mi app
print("==============================")
print("Train Boost: tu app de confianza")
print("==============================")

nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
peso = float(input("¿Cuál es tu peso en kg? "))
estatura = float(input("¿Cuánto mides en cm? "))
objetivo = input("¿Cuál es tu objetivo? (Ganar músculo, perder grasa o mantenerme): ")
nivel = input("¿Cuál es tu nivel? (Principiante, intermedio o avanzado): ")
dias = input("¿Cuántos días a la semana puedes entrenar? ")
lugar = input("¿Entrenas en casa o en un gimnasio? ")

print("==============================")
print("¡Bienvenido a Train Boost,", nombre, "!")
print("Vamos a trabajar para alcanzar tu objetivo.")
print("==============================")

while True:
    print("\n========== MENÚ ==========")
    print("1. Ver mis datos")
    print("2. Calcular IMC")
    print("3. Ver mi objetivo")
    print("4. Salir")
    print("==========================")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\n--- Mis datos ---")
        print("Nombre:", nombre)
        print("Edad:", edad, "años")
        print("Peso:", peso, "kg")
        print("Estatura:", estatura, "cm")
        print("Nivel:", nivel)
        print("Días para entrenar:", dias)
        print("Lugar de entrenamiento:", lugar)

    elif opcion == "2":
        if peso > 0 and estatura > 0:
            imc = peso / ((estatura / 100) ** 2)
            print("Tu IMC es:", round(imc, 2))
        else:
            print("El peso y la estatura deben ser mayores que cero.")

    elif opcion == "3":
        print("Tu objetivo es:", objetivo)

    elif opcion == "4":
        print("¡Gracias por usar Train Boost!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
