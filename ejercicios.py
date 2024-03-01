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
letras = ['abcdefghijklmnñopqrstuvwxyz']
caracteres =['a','e','i', 'o','u', ' ', ',','.' ]
estadisticas = ['Total de caracteres:', 'Total de letras : ', 'Total de vocales a :', 'Total de vocales e :', 'Total de vocales i :', 'Total de vocales o :', 'Total de vocales u :', 'Total de espacios :', 'Total de comas', 'Total de puntos']
totales = [1,1,0,0,0,1,0,0,0,0]


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
total de puntos :


1. Crear lista cadenaLarga
2. Crear lista caracteres
3. Crear lista de estadisticas
4. Crear lista totales
5. Recorrer cadenaLarga
6.      Ir acumulando los valores de totales según caracteres
7. Imprimir totales tomando los valores de las listas 'estadisticas' y 'totales'

"""
print(cadenaLarga)
