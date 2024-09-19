print (" -- CLASES V2 -- ")


# ZONA DE CLASE
class Datos:
    #EL CONSTRUCTOR FUNCIÓN
    def __init__(self, estatura, peso):
        self.estatura=estatura
        self.peso=peso
    
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts, {self.peso} Kg")

# LISTAS
    def mi_lista(self):
        sabores=["Vainilla", "Chocolate", "Fresa", "Limon"]
        print(sabores)
        for saa in sabores:
            print(saa)

# TUPLAS 
    def mi_tupla(self):
        paises=("Mexico", "Colombia", "Estados Unidos", "España")
        print(paises)
        for pai in paises:
            print(pai)

# CONJUNTOS 
    def mi_conjunto(self):
        colores={"Rojo", "Verde", "Azul", "Blanco"}
        print(colores)
        for col in colores:
            print(col)

# DICCIONARIOS 
    def mi_diccionario(self):
        celular={
        "Marca":"Samsung",
        "Modelo":"S22",
        "Año":2022}
        print(celular)
        for cel in celular:
            print(cel)

# CREACION DE OBJETO
info=Datos(1.60, 54.2)

#UTILIZACION DE OBJETOS
info.mostrar_datos()
print(" -- LISTA DE MARCAS DE SABORES DE HELADOS -- ")
info.mi_lista()
print(" -- TUPLA DE MARCAS DE PAISES -- ")
info.mi_tupla()
print(" -- CONJUNTO DE MARCAS DE COLORES -- ")
info.mi_conjunto()
print(" -- DICCIONARIO CON INFORMACION DE CELULAR -- ")
info.mi_diccionario()
