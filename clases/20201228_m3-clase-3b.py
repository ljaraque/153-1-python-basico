from uuid import uuid4

class Empleado:
    
    def __init__(self, nombre, sueldo, cargo):
        self.id = uuid4()
        self.nombre = nombre
        self.sueldo = sueldo
        self.cargo = cargo

    def genera_reporte_semanal(self):
        return "Este es mi reporte"
    
    def renunciar(self):
        return "No vuelvo más"

    def cobrar_sueldo(self):
        return "Estoy cobrando poca plata"


class Especialista(Empleado):

    def viajar_a_rusia(self):
        return "Viajando en avión por 36 horas"


especialista_1 = Especialista("Tom Araya", 3000000, "Diseñador de Chips")

for atributo_metodo in dir(especialista_1):
    print(atributo_metodo)

