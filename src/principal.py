


if __name__ == '__main__':
    # TODO: Aquí va el código que inicializa tu aplicación.

    def main():
        libro = libro ("La historia del bicho", 2023 , "Cristiano Ronalgon", 450)
        revista = revista("Lo reviso luego", 2023, 210, "Su publicacion")

        print("Informacion del libro:")
        libro.mostrar_info()

        print("Informacion de la revista")
        revista.mostrar_info()