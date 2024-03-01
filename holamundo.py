# Esta es mi primera aplicación en Python
print("Hola mundo")
print("Bienvenido a Python")
print("___________________")
print("Variables en Python")

# Tipos de datos en variables
nombre = "Esdras"   # cadena
edad = 24           # numérico entero
correo = "esdras@upb.edu.mx"   # cadena
promedio = 8.7      # numérico de punto flotante 
beca = False        # booleano

# Imprimir los datos
print("Nombre :",nombre)
print("Tipo de dato de la variable Nombre : ",type(nombre))

print("edad :",edad)
print("Tipo de dato de la variable edad : ",type(edad))

print("promedio :",promedio)
print("Tipo de dato de la variable promedio : ",type(promedio))

print("beca :",beca)
print("Tipo de dato de la variable beca : ",type(beca))


#Operadores: +, -, *, /, % (residuo), // (división entera), ** (exponente)
potencia2 = 2**10
residuo = 105 % 6

print(potencia2)
print(residuo)

# condiciones if-else (operadores ==, >, >=, <, <=, !=)
edad = 12
if edad >= 18:
    print("Puede votar")
    print("Espero verte este 6 de junio")
else:
    print("No puede votar")
    print("Tan pronto tengas la edad, solicita tu INE")


# Listas en python
# Es  un arreglo de elementos del cual la lista puede ser actualizada
alumnos = ["Valentin", "Rosendo", "Valentin2", "Lilia", "Dani", "Alan", "Jonathan","Manzo"]
print(type(alumnos))

print(alumnos)

#Imprimir elementos individuales, con el índice iniciando desde 0
print(alumnos[0])
print(alumnos[3])
print(alumnos[4])
print(alumnos[5])
print("------------------------")
#imprimir los elemntos en un ciclo, recorrer la lista
i = 0
for elemento in alumnos:
    print(i,":",elemento)
    i=i+1

for i in range (100,110,2):
    print(i)


# hacer el juego del Gato en Python, usando una lista para almacenar las posiciones
# Versión 1 : 2 jugadores
# Version 2: Jugador vs maquina


# while 
print("while")
print("Elementos de la lista2")
lista2 = ["pantalla", "teclado", "bocinas", "mouse", "usb", "cd", "quemador", "impresora", "microfono", "webcam"]
print(lista2)

# Recorrer la list2 con while
i = 0
while i < len(lista2):
    print(i, ":", lista2[i])
    i=i+1

# acceder a los elementos de la lista2 por medio de indices
print("La lista2 tiene ", len(lista2), " elementos")
print("Todos los elementos 0-9 ", lista2[0:10])
print("Elmentos del 2-6 ", lista2[2:7])
print("Elementos desde el 5 hasta el último ", lista2[5:])
print("Imprimir los primeros 3 elementos ", lista2[:3])

# Realizar los siguientes ejercicios
# 1. Extraer 'mouse', 'usb', 'cd', 'quemador', 'impresora' con indices
# 2. extraer   'mouse', 'usb', 'cd', 'quemador', 'impresora', 'microfono', 'webcam'
# 3. extraer 'pantalla', 'teclado', 'bocinas', 'mouse', 'usb', 'cd', 'quemador', 'impresora'
# 4. extraer 'pantalla', 'bocinas',  'usb', 'quemador', 'microfono'
# 5. Programar para extraer de lista2, la sublista equipo = ['mouse', 'cd', 'microfono', 'cargador'] , que aparezca sú número de índice de cada uno
#    Resultado esperado:
#    Indice 3 : mouse
#    Indice 5 : cd
#    Indice 8 : microfono
#    Cargador NO encontrado en lista2
lista2 = ["pantalla", "teclado", "bocinas", "mouse", "usb", "cd", "quemador", "impresora", "microfono", "webcam"]
equipo = ['mouse', 'cd', 'microfono', 'cargador']




cadenaLarga = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc placerat egestas egestas. Morbi malesuada eros sed odio mattis luctus ut quis libero. Nunc tincidunt sapien at congue sodales. Praesent a maximus libero. Proin sed placerat elit, condimentum vulputate nunc. Quisque et sodales nisi. Nulla elementum ex in odio ultrices malesuada. Praesent dictum ante sit amet enim semper scelerisque. Pellentesque eros massa, dapibus at mi eget, ullamcorper aliquet leo. Nulla id lacus id dui convallis dapibus. Aliquam vitae mattis leo. Vivamus elementum, metus elementum eleifend vehicula, magna enim consequat ante, imperdiet blandit elit diam sed urna. Vivamus finibus maximus elit ut laoreet. Aliquam fringilla rhoncus dapibus. Donec in consequat lorem. Sed vestibulum facilisis egestas.

Proin in convallis augue. Vestibulum elementum nibh et urna pellentesque, quis blandit tortor tempor. Vivamus tristique condimentum rutrum. Aliquam at odio facilisis, convallis lorem sit amet, posuere odio. Integer aliquet in felis tristique scelerisque. Duis finibus at velit in eleifend. Integer sed ligula consectetur, sollicitudin nisl at, tempor purus. Curabitur consequat ante nec lorem interdum feugiat. Etiam sagittis ornare ex, vitae tempus purus commodo eget. Curabitur tempor dui nunc, at ultrices ligula condimentum eget. Mauris ac ante viverra, sodales arcu eget, mattis mi. Pellentesque condimentum hendrerit sem. Sed tincidunt bibendum augue a dapibus. Nam quis eleifend magna.
"""
print(cadenaLarga)
caracteres =``['a', 'e','i', 'o','u', ' ', ',' ]` 

"""
Dada una cadena larga (lorem ipsum de 5 párrafos)
Presentar un resumen de las estadística de los párrafos
Total de caracteres:
Total de letras : 
Total de vocales a :
Total de vocales e :
Total de vocales i :
Total de vocales o :
Total de vocales u :
Total de espacios :
Total de comas :
Total de palabras :
"""

