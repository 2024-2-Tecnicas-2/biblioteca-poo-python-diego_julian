class Publicacion:
    def __init__(self,titulo, anio_publicacion):
     self.titulo = titulo
     self.anio_publicacion = anio_publicacion

    def mostrar_info(self):
        print("Titulo:",{self.titulo})
        print("Año de publicacion:",{self.anio_publicacion})
