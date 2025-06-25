# Nombre: Matías Marin
# Descripción: programacion orientada a objetos

def ingresar_usuario(usuarios):
    while True:  # Este bucle repite todo el proceso hasta que el usuario se ingrese correctamente
        try:
            # Bucle para repetir hasta que el nombre de usuario sea válido y no exista
            while True:
                nombre = input("Ingrese Nombre de usuario:")  # Solicita el nombre del usuario
                if nombre in usuarios:
                    print("Error: usuario ya existe. Intente otro.")
                    continue  # Si ya existe, vuelve a pedir el nombre
                break  # Si es válido, sale del bucle

            # Bucle para repetir hasta que el sexo sea válido
            while True:
                sexo = input("Ingrese sexo (F/M): ")  # Solicita el sexo
                if sexo not in ("F", "M"):
                    print("Error: sexo inválido. Debe ser 'F' o 'M'.")
                    continue  # Si es inválido, vuelve a pedir el sexo
                break  # Si es válido, sale del bucle

            # Bucle para repetir hasta que la contraseña sea válida
            while True:
                contraseña = input("Ingrese contraseña: ")  # Solicita la contraseña
                if (len(contraseña) < 8 or
                    not any(caracter.isdigit() for caracter in contraseña) or
                    not any(caracter.isalpha() for caracter in contraseña) or
                    " " in contraseña):
                    print("Error: Contraseña no valida.")
                    continue  # Si es inválida, vuelve a pedir la contraseña
                break  # Si es válida, sale del bucle

            # Si todo es válido, guarda el usuario y sale del bucle principal
            usuarios[nombre] = {"sexo": sexo, "contraseña": contraseña}
            print("Usuario ingresado con exito.")
            break  # Sale del bucle principal y vuelve al menú

        except Exception as error_general:
            # Si ocurre un error inesperado, muestra el error y repite todo el proceso
            print("Error inesperado al ingresar los datos:", error_general)

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

