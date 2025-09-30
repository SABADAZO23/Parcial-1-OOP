class Libro:
    def __init__(self, titulo,autor,categoria):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponible = True
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return  f"{self.titulo} - {self.autor}({self.categoria}) -> {estado}"
    
#Clase Libros