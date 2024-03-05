def saludo(mensaje="Mundo!"):
    print("Hola")
    print(f"{mensaje}")

saludo()
saludo("John Doe")



def suma(a, b):
    return (a + b)

resultado = suma(10 , 5)
print(resultado)

resultado = suma()
print(resultado)

resultado = suma(11)
print(resultado)