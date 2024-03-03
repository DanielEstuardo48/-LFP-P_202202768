import re
import os
import graphviz

class Peliculas:
    def __init__(self, nombre, actor, anio, genero):
        self.nombre = nombre
        self.actor = actor
        self.anio = anio
        self.genero = genero

class Peliapp:
    def __init__(self):
        self.peliculas = []
    
    def carga_archivo(self):
        archivo = r'C:\Users\danis\OneDrive\Documents\Quinto Semestre\LFP\Practica1[LFP]\PRUEBA.lfp'
        try:
            with open(archivo, "r") as f:
                peliculas_rep = {}
                for linea in f:
                    nombre, actor, anio, genero = linea.strip().split(';')
                    pelicula = Peliculas(nombre, actor, int(anio), genero)
                    if nombre not in peliculas_rep:
                        peliculas_rep[nombre] = pelicula
                self.peliculas = list(peliculas_rep.values())
                print("\nArchivo cargado correctamente")
        except FileNotFoundError:
            print("\nEl archivo no existe. ")

    def gestionar_pelicula(self):
        if not self.peliculas:
            print("\nError: No se puede acceder a esta opción porque no se ha cargado ningun elemento previamente")
        else:
            while True:
                print("\n================ Gestionar películas =============")
                print("1. Mostrar peliculas")
                print("2. Mostrar Actores")
                print("3. Regresar el Menu Principal")
                opcion = int(input("Ingrese una opción: "))

                if opcion == 1:
                    self.mostrar_peliculas()
                elif opcion == 2:
                    self.mostrar_actores()
                elif opcion == 3:
                    break
                else:
                    print("\nError: opción invalida")
    
    def mostrar_peliculas(self):
        print("\n============================= Las peliculas Registradas son: ======================================")
        name_width = max(len(pelicula.nombre) for pelicula in self.peliculas) + 2
        year_width = max(len(str(pelicula.anio)) for pelicula in self.peliculas) + 2
        genre_width = max(len(pelicula.genero) for pelicula in self.peliculas) + 2
        actors_width = max(len(pelicula.actor) for pelicula in self.peliculas) + 2
        print('\n{nombre:<{width}} {anio:<{width}} {genero:<{width}} {actor:<{width}}'.format(
        nombre='Nombre', anio='Año', genero='Genero', actor='Actores', width=name_width,))
        print('-' * (name_width + year_width + genre_width + actors_width))
        for pelicula in self.peliculas:
            print('{nombre:<{width}} {anio:<{width}} {genero:<{width}} {actor:<{width}}'.format(
            nombre=pelicula.nombre, anio=pelicula.anio, genero=pelicula.genero, actor=pelicula.actor,
            width=name_width,))

    def mostrar_actores(self):
        print("\n========================= Las peliculas Registradas son: ==============================")
        for index, pelicula in enumerate(self.peliculas):
            print(f'{index+1}.{pelicula.nombre}')
        opcion = int(input("Seleccione el numero de la pelicula que desea: "))
        if opcion in range (1,index+2):
            print("\nLos actores que participaron en esta pelicula son los siguientes: ", pelicula.actor)
        else:
            print("\nError: El numero ingresado no pertenece a ninguna pelicula.")
    
    def filtrado(self):
        if not self.peliculas:
            print("\nError: No se puede acceder a esta opción porque no se ha cargado ningun elemento previamente")
        else:
            while True:
                print("\n======================== Filtrado de películas ===========================")
                print("1. Filtrar por actor")
                print("2. Filtrar por año")
                print("3. Filtrar por género")
                print("4. Regresar al menu principal")
                opcion = int(input("Ingrese una opción: "))

                if opcion == 1:
                    self.filtrar_actor()
                elif opcion == 2:
                    self.filtrar_anio()
                elif opcion == 3:
                    self.filtrar_genero()
                elif opcion == 4:
                    break
                else:
                    print("\nError: opción no valida")
    
    def filtrar_actor(self):
        print("\n================= Filtrado por Actor ====================")
        while True:
            actorp = input("\nIngrese el nombre del actor: ")
            if re.match(r'^[a-zA-Z\s]*$', actorp):
                break
            else:
                print("\nError: no puede ingresar numeros.")
        actores = self.buscar_actor(actorp)

        if actores:
            print(f"\nEL actor {actorp} participa en las siguientes peliculas: ")
            for index, pelicula in enumerate(actores):
                print(f'\n{index+1}. {pelicula.nombre}')
        else:
            print(f"\nError: No se encontraron las peliculas en que participa {actorp}")
    
    def buscar_actor(self, actorp):
        actores = []
        for pelicula in self.peliculas:
            if actorp in  pelicula.actor:
                actores.append(pelicula)
        return actores
    
    def filtrar_anio(self):
        print("\n================= Filtrado por Año ====================")
        anio = int(input("\nIngrese el año: "))
        anios = self.buscar_anio(anio)

        if anios:
            print(f"\nEn el año {anio} se estrenaron las siguientes peliculas: ")
            for index, pelicula in enumerate(anios):
                print(f'\n{index+1}. Nombre: {pelicula.nombre},    Género: {pelicula.genero}')
        else:
            print(f"\nError: No se encontraron las peliculas estrenadas en el año: {anio}")

    def buscar_anio(self, anio):
        anios = []
        for pelicula in self.peliculas:
            if int(pelicula.anio) == anio:
                anios.append(pelicula)
        return anios

    def filtrar_genero(self):
        print("\n============================= Filtrado por Género ======================")
        while True:
            generop = input("\nIngres el género que desea buscar: ")
            if re.match(r'^[a-zA-Z\s]*$', generop):
                break
            else:
                print("\nError: No puede ingresar numeros.")
        generos = self.buscar_genero(generop)
        
        if generos:
            print(f"\n El las peliculas que pertenecen al género {generop} son: ")
            for index, pelicula in enumerate(generos):
                print(f'\n{index+1}. {pelicula.nombre}')
        else:
            print(f"\nError: No se encontrar peliculas con el género {generop}")
    
    def buscar_genero(self, genero):
        generos = [] 
        for pelicula in self.peliculas:
            if genero in pelicula.genero:
                generos.append(pelicula)
        return generos
    
    def grafica(self):
        for pelicula in self.peliculas:
            contenido_dot = """
            import Main
            digraph G {
            fontname = "Helvetica,Arial,sans-serif"
            graph [
                rankdir = "LR"
            ];

            node [shape = plaintext];
            tabla1 [label =<
                <TABLE BORDER="0" CELLBORDER ="1" CELLSPACING = "0">
                    <TR>
                        <TD COLSPAN = "2" BGCOLOR = "darkgreen"><FONT COLOR = "white"> pelicula.nombre </FONT></TD>
                    </TR>
                    <TR>
                        <TD>pelicula.anio</TD>
                        <TD>pelicula.genero</TD>
                    </TR>
                </TABLE>
            >];

            node[shape=box, style = filled, fillcolor=darkmagenta, fontcolor = white];
            peliculaactor [label="pelicula.actor"];

            tabla1 -> peliculaactor;
            }
            """
            nombre_dot = "pelicula.dot"

        for pelicula in self.peliculas:
                with open( r'C:\Users\danis\OneDrive\Documents\Quinto Semestre\LFP\Practica1[LFP]\pelicula.dot',"w") as archivo_dot:
                    archivo_dot.write(contenido_dot)
        print(f'Archivo DOT {nombre_dot} creado')
        # Obtener el directorio actual
        dir_actual = os.getcwd()
        # Cambiar al directorio que contiene los archivos
        os.chdir(r'C:\Users\danis\OneDrive\Documents\Quinto Semestre\LFP\Practica1[LFP]')
        # Definir los nombres de los archivos
        nombre_dot = "pelicula.dot"
        nombre_pdf = "pelicula.pdf"
        # Ejecutar el comando dot
        os.system(f"dot -Tpdf \"{nombre_dot}\" -o \"{nombre_pdf}\"")
        # Regresar al directorio original
        os.chdir(dir_actual)
        print(f"Archivo PDF '{nombre_pdf}' creado satisfactoriamente.")   

def mensaje_inicial():
    print("\n===== Lenguajes Formales y de Programación ====")
    print("Sección: P")
    print("Carné: 202202768")
    print("Nombre: Daniel Estuardo Salvatierra Macajola")
    input("\nPresione enter para continuar... ")

def menu():
    print("\n========== Menu principal ===========")
    print("Seleccione una opción: ")
    print("1. Cargar archivo de entrada")
    print("2. Gestionar películas")
    print("3. Filtrado")
    print("4. Gráfica")
    print("5. Salir")

def main():
    peliapp = Peliapp()
    mensaje_inicial()
    while True:
        menu()
        opcion = int(input("\nSeleccione una opción: "))
        if opcion == 1:
            peliapp.carga_archivo()
        elif opcion == 2:
            peliapp.gestionar_pelicula()
        elif opcion == 3:
            peliapp.filtrado()
        elif opcion == 4:
            peliapp.grafica()
        elif opcion == 5:
            print("\nGracias por usar el programa!")
            print("Saliendo...")
            break
        else:
            print("Error: opción no disponible")


if __name__ == "__main__":
    main()
