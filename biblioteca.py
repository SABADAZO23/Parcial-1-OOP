from libro import Libro
from usuario import Usuario 

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
    
    def registrar_libros(self, titulo,autor,categoria):
        libro = Libro(titulo,autor,categoria)
        self.libros.append(libro)
        print(f"libro '{titulo}' registrado en la categoria '{categoria}'.")

    def registrar_usuarios(self,nombre,id_usuario):
        usuario = Usuario(nombre,id_usuario)
        self.usuarios.append(usuario)
        print(f"Usuario '{nombre}' registrado con ID {id_usuario}")

    def mostrar_libros(self):
        print("\n Lista de libros en la biblioteca: ")
        for libro in self.libros:
            print(libro)

    def mostrar_usuarios(self):
        print("\n Lista de usuarios registrados en la Biblioteca")
        for usuario in self.usuarios:
            print(usuario)

    def prestar_libro(self,titulo,id_usuario):
        libro = next ((l for l in self.libros if l.titulo == titulo and l.disponible), None)
        usuario = next((u for u in self.usuarios if u.id_usuario == id.usuario), None)

        if libro and usuario:
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            print(f"Libro '{titulo}' prestado a {usuario.nombre}.")
        else:
            print("No se pudo prestar el libro revisar disponibilidad ")

    def devolver_libros(self,titulo, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario), None)
        if usuario:
            libro = next ((l for l in usuario.libros_prestados if l.titulo == titulo), None)   
            if libro:
                libro.disponible = True
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{titulo}' devuelto por {usuario.nombre}. ")
                return
        print("No se pudo devolver el libro. ")    
    

        