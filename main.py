from representante import Representante

def ingresar_representantes():
    lista_representantes = []
    while True:
        nombre = input("Ingrese el nombre del representante: ")
        edad = int(input("Ingrese la edad del representante: "))
        direccion = input("Ingrese la dirección del representante: ")
        empresa = input("Ingrese la empresa donde trabaja: ")

        representante = Representante(nombre, edad, direccion, empresa)
        lista_representantes.append(representante)

        continuar = input("¿Desea ingresar otro representante? (s/n): ").lower()
        if continuar != 's':
            break

    return lista_representantes

def mostrar_representantes(lista_representantes):
    if lista_representantes:
        print("\nRepresentantes ingresados:")
        for representante in lista_representantes:
            print(representante.mostrar_datos())
    else:
        print("No se han ingresado representantes.")

if __name__ == "__main__":  
    representantes = ingresar_representantes()
    mostrar_representantes(representantes)
