# Nombre: Matías Marin
# Descripción: programacion orientada a objetos

def ingresar_usuario(usuarios):
    nombre = input("Ingrese Nombre de usuario:")  # Solicita el nombre del usuario
    if nombre in usuarios:  # Verifica si el nombre ya existe como clave en el diccionario usuarios
        print("Error: usuario ya existe.")
        return
    sexo = input("Ingrese sexo (F/M): ")  # Solicita el sexo
    if sexo not in ("F", "M"):  # Verifica que el sexo sea F o M
        print("Error: sexo inválido. Debe ser 'F' o 'M'.")
        return
    contraseña = input("Ingrese contraseña: ")  # Solicita la contraseña

    # Validaciones de la contraseña:
    # len(contraseña) < 8: verifica que la contraseña tenga al menos 8 caracteres
    # any(c.isdigit() for c in contraseña): verifica que haya al menos un número en la contraseña
    # any(c.isalpha() for c in contraseña): verifica que haya al menos una letra en la contraseña
    # " " in contraseña: verifica si hay espacio en blanco en la contraseña
    if (len(contraseña) < 8 or
            not any(c.isdigit() for c in contraseña) or
            not any(c.isalpha() for c in contraseña) or
            " " in contraseña):
        print("Error: Contraseña no valida.")
        return

    # usuarios[nombre] = {...} agrega una nueva clave (nombre) al diccionario usuarios,
    # y como valor le asigna otro diccionario con los datos del usuario.
    usuarios[nombre] = {"sexo": sexo, "contraseña": contraseña}
    print("Usuario ingresado con exito.")

def buscar_usuario(usuarios):
    nombre = input("Ingrese nombre de usuario a buscar: ")  # Solicita el nombre a buscar
    if nombre in usuarios:  # Verifica si el nombre existe como clave en el diccionario usuarios
        # usuarios[nombre]['sexo'] accede al valor de la clave 'sexo' dentro del diccionario del usuario
        print(f"Sexo: {usuarios[nombre]['sexo']}")
        print(f"Contraseña: {usuarios[nombre]['contraseña']}")
    else:
        print("El usuario no se encuentra.")

def eliminar_usuario(usuarios):
    nombre = input("Ingrese nombre de usuario a eliminar: ")  # Solicita el nombre a eliminar
    if nombre in usuarios:  # Verifica si el nombre existe como clave en el diccionario usuarios
        del usuarios[nombre]  # Elimina la clave (usuario) del diccionario usuarios
        print("Usuario eliminado con exito")
    else:
        print("No se pudo eliminar el usuario. Ingrese usuario valido.")

def menu():
    usuarios = {}  # Crea un diccionario vacío para almacenar los usuarios
    while True:  # Bucle infinito para mostrar el menú hasta que el usuario decida salir
        print("\nMenú de gestion de usuarios")
        print("1. Ingresar usuario")
        print("2. Buscar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")  # Solicita la opción del menú
        if opcion == "1":
            ingresar_usuario(usuarios)  # Llama a la función para ingresar usuario
        elif opcion == "2":
            buscar_usuario(usuarios)  # Llama a la función para buscar usuario
        elif opcion == "3":
            eliminar_usuario(usuarios)  # Llama a la función para eliminar usuario
        elif opcion == "4":
            print("Programa terminado...")
            break  # Sale del bucle y termina el programa
        else:
            print("Debe ingresar una opcion valida!!")

if __name__ == "__main__":  # Esto asegura que el menú solo se ejecute si el archivo es el principal
    menu()

