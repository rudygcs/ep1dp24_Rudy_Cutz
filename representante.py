from persona import Persona 

class Representante(Persona): 
    def __init__(self, nombre, edad, direccion, empresa): 
        super().__init__(nombre, edad, direccion) 
        self.empresa = empresa 
    def mostrar_datos(self): 
        datos_persona = super().mostrar_datos() 
        return f'{datos_persona}, Empresa: {self.empresa}' 
