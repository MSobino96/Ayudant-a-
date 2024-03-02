print("\nHola, Bienvenido a nuestra pagina.\n")

nombres = ['Leonidas','Claudio','Ricardo','Matias']

nombre_usuario = input("ingrese su nombre: ")

if nombre_usuario.capitalize() in nombres:
    print(f"Hola {nombre_usuario.capitalize()}, Bienvenido")
else:
    print(f"Lo siento, {nombre_usuario.capitalize()}, no te encuentro en nuestra lista \n")

#len

print(f'La cantidad de usuarios en la lista es: {len(nombres)}')

print('Saludo a todos los usuarios')
for nombre in nombres:
    print(f'Hola {nombre}!')




