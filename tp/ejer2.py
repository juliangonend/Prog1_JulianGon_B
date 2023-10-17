def cambiar_mayusculas_minisculas(palabra):
    return palabra.swapcase()

# Solicitar al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")

# Llamar a la función para invertir mayúsculas y minúsculas
resultado = cambiar_mayusculas_minisculas(palabra)

# Mostrar el resultado
print("Resultado:", resultado)
