# =============================================================
# Tema 01 · Variables, tipos, entrada y salida · EJERCICIOS
# python-adso · SENA ADSO
#
# INSTRUCCIONES
#   1. Copia este archivo al repositorio de TU app como:
#        ejercicios/tema-01.py
#   2. Resuelve cada ejercicio debajo de su enunciado.
#   3. Ejecuta el archivo y prueba que todo funcione.
#   4. Súbelo a GitHub con el commit:
#        feat: tema 01 y bienvenida de la app
#
# Nombre completo: Mateo Pabon Bedoya
# Mi app se llama:Trainboost
# =============================================================


# -------------------------------------------------------------
# EJERCICIO 1 · Tarjeta de presentación
# -------------------------------------------------------------
# Crea tres variables: tu nombre (texto), tu edad (entero) y tu
# estatura en metros (decimal). Muestra las tres con UN solo print
# usando f-string.
#
# Así debe verse:
#   Soy Ana, tengo 19 años y mido 1.62 m.

# Tu código aquí:

nombre = "mateo"
edad = 17
altura = 1.78

print(f"soy {nombre}, tengo {edad} y mido {altura}")



# -------------------------------------------------------------
# EJERCICIO 2 · ¿De qué tipo es?
# -------------------------------------------------------------
# Crea estas cuatro variables y muestra el tipo de cada una con type():
#   a = "100"
#   b = 100
#   c = 100.0
#   d = "cien"
#
# Después, en un comentario, responde: ¿por qué "100" y 100 no son
# lo mismo para Python?

# Tu código aquí:

a = "100"
b = 100
c = 100.0
d = "cien"

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# Respuesta: por que cuando algo dato tiene comillas automaticamente se vuelve tipo de dato texto



# -------------------------------------------------------------
# EJERCICIO 3 · La cuenta del almuerzo
# -------------------------------------------------------------
# Pregunta con input():
#   - el valor de la cuenta
#   - cuántas personas van a pagar
#   - el porcentaje de propina (por ejemplo 10)
#
# Muestra: el valor de la propina, el total con propina y cuánto
# paga cada persona. Los valores en pesos, con separador de miles.
#
# Así debe verse (si escriben 85000, 3 y 10):
#   Propina:          $8,500
#   Total:            $93,500
#   Cada uno paga:    $31,167

# Tu código aquí:

valor_cuenta = float(input("Valor de la cuenta: "))
personas = int(input("¿Cuántas personas van a pagar? "))
porcentaje_propina = float(input("Porcentaje de propina"))

valor_propina = valor_cuenta * porcentaje_propina / 100
total = valor_cuenta + valor_propina
pago_por_persona = total / personas

print(f"Propina:          ${valor_propina:,.0f}")
print(f"Total:            ${total:,.0f}")
print(f"Cada uno paga:    ${pago_por_persona:,.0f}")


# -------------------------------------------------------------
# EJERCICIO 4 · Encuentra el error
# -------------------------------------------------------------
# Este código tiene 2 errores. Corrígelos y explica en un
# comentario qué estaba mal en cada uno.
#
#   precio = input("Precio del producto: ")
#   unidades = input("Unidades: ")
#   print("Total a pagar: " + precio * unidades)

#Tu código corregido aquí:
precio = float(input("Precio del producto: "))
unidades = int(input("Unidades: "))
print("Total a pagar: " + str(precio * unidades))


# Error 1: la variable precio y unidades no tienen especificados que tipo de dato son, el sistema los toma como texto
# Error 2:cuando hace print se intentaba concatenar un texto con un número usando
# + y por lo que busque Python no permite sumar str + float/int. )Hay que convertir
# el resultado a texto con str()


# -------------------------------------------------------------
# EJERCICIO 5 · Inventario rápido
# -------------------------------------------------------------
# Pregunta el nombre de un producto, cuántas unidades hay y el
# precio de cada unidad. Muestra un resumen como este:
#
#   ===== INVENTARIO =====
#   Producto:   Tabla de pino
#   Unidades:   40
#   Precio:     $18,000
#   Valor total: $720,000
#   ======================

# Tu código aquí:

producto = input("nombre del producto: ")
unidades = int(input("cuantas unidades llevaras: "))
precio = float(input("precio de cada unidad: "))

total = unidades * precio

print(f"producto: {producto}")
print(f"unidades: {unidades}")
print(f"precio: ${precio:,.0f}")
print(f"valor total: ${total:,.0f}")



# =============================================================
# EJERCICIO 6 · LLÉVALO A TU APP  (va en tu app.py, no aquí)
# =============================================================
# En el archivo app.py de tu proyecto, crea la pantalla de bienvenida
# de tu app. Debe:
#   1. Mostrar el nombre de tu app con un encabezado visible.
#   2. Preguntarle al usuario al menos 2 datos con input()
#      (por ejemplo: su nombre y algo que tenga sentido en tu app).
#   3. Responder con un mensaje que use esos datos (f-string).
#   4. Al menos un dato debe ser un número con el que hagas una cuenta.
#
# Ejemplo para una app de citas de barbería:
#   ==============================
#        BARBERÍA EL CORTE
#   ==============================
#   ¿Cómo te llamas? Carlos
#   ¿Cuántos cortes quieres agendar? 2
#   Hola Carlos, tus 2 cortes cuestan $50,000.
#
# Este es el primer paso de tu app: en los próximos temas le
# agregamos el menú, las listas y todo lo demás.
# =============================================================
