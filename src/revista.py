from src.publicacion import Publicacion


class Revista(Publicacion):
    
    def __int__ (self,titulo, anio_publicacion, numero_revista, nombre_revista):
        super().__init__(titulo, anio_publicacion)
        self.numero_revista = numero_revista
        self.nombre_revista = nombre_revista
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Numero de la revista: ",{self.nombre_revista})
        print("Nombre de la revista",{self.nombre_revista})
