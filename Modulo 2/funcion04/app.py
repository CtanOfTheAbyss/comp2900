def saludo():
    global nombre 
    nombre ="John Doe"
    print(f'Hola {nombre}')

def despedida():
    # global nombre
    nombre ="Saul Bruhman"
    print(f'Adios {nombre}')

saludo()
despedida()
print(nombre)
