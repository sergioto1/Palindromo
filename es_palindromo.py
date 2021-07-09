'''
Verificar si un texto que termina en punto es un palíndromo (capicúa). Un texto es
palíndromo si se lee lo mismo de izquierda a derecha o de derecha a izquierda. 
Ej: “Amor a roma”.
'''
def es_palindromo (texto: str) -> str:
    texto = texto.lower() #pasar a minuscula
    if (texto[-1] == "."):       # condición: si el último caracter es un punto 
        texto = texto[:-1]       # reasignar variable sin el punto
        print(texto[::-1])       # mostrar el string de der a izq para comprobar  
        return "Es un palindromoo"
    elif (texto == texto[::-1]): # condicion: si la cadena es un palindromo
        print(texto[::-1]) # mmostra el string de der a izq
        return "Es un palindromo"
    else: # si no concuerda entonces no es palindromo
        print(texto[::-1])
        return "No es un palindromo"

#pruebas
print(es_palindromo('Amor a roma.'))
print(es_palindromo('HanNaH'))

