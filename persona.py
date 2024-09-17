class Persona: # definir clase persona
    def __init__(self, nombre, edad, direccion): # Este es el constructor de la clase. Se ejecutara cada vez que creamos un nuevo objeto de tipo Persona. Los parámetros nombre, edad y direccion son los atributos de la persona.
        self.nombre = nombre # asigna el valor del nombre ingresado al atributo nombre del objeto.
        self.edad = edad # igual que la de arriba
        self.direccion = direccion # igual que la de arriba

    def mostrar_datos(self): # método que devuelve una cadena de texto con la información de la persona.
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}' # Utiliza una cadena formateada (f-string) para mostrar los datos del objeto.
