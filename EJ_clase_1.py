print("Introduccion a clases")
class animal:
    edad=3
    raza="Chihuahua"
    def come():
        lacomida="Croquetas"
        return lacomida
print("Creando el objeto de la clase animal")
perro=animal()
print(f"Edad del perro: {perro.edad}")
print(f"Raza del perro: {perro.raza}")
print(f"El perro come: {animal.come()}")