from biblioteca import Biblioteca
def menu():
    print("\n ---- Menu Biblioteca ----")
    print("1. Registrar libro")
    print("2. Regitrar usuarios")
    print("3. Mostrar libros")
    print("4. Mostrar usuario ")
    print("5. Prestar libro ")
    print("6. Devolver libro ")
    print("0. Salir")
    return input("Seleccione una opcion: ")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    categorias = ["Ciencia", "Ciencia Ficcion", "Fantasia", "Historia", "Misterio"]

    while True:
        opcion = menu()

        if opcion == "1":
            titulo = input("titulo: ")
            autor =input("autor: ")
            print("Categorias disponibles: ", categorias)
            categoria = input("Categorias: ")
            biblioteca.registrar_libros(titulo, autor, categoria)
            print("El resgistro fue exitoso ")
        
        elif opcion == "2":
            usuario = input("Nombre: ")
            id_usuario = input("ID: ")
            biblioteca.registrar_usuarios(usuario, id_usuario)
            print("El usuario fue registrado con exito: ")

        elif opcion == "3":
            biblioteca.mostrar_libros()
        
        elif opcion == "4":
            biblioteca.mostrar_usuarios()

        elif opcion == "5": 
            titulo = input("Titulo del libro para prestamo: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.prestar_libro(titulo, id_usuario)
        elif opcion == "6":
            titulo = input("titulo del libro a devolver: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.devolver_libros(titulo, id_usuario)
        elif opcion == "0":
            print("Saliendo del programa.................... ")
            break
        else:
            print("Opcion no valida")
