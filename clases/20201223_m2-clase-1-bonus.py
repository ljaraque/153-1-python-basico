from uuid import uuid4

class Cliente:

    def __init__(self, nombre, saldo):
        self.__id = uuid4()
        self.__nombre = nombre
        self.__saldo = saldo
        self.__atributos = self.atributos
    
    def girar(self, monto):
        self.__saldo -= monto
        return self.__saldo
    
    def abonar(self, monto):
        self.__saldo += monto
        return self.__saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def id(self):
        return self.__id
    
    @property
    def nombre(self):
        return self.__nombre
        
    @property
    def atributos(self):
        lista_atributos = list()
        for atributo in dir(self):
            if atributo[0]!="_":
                lista_atributos.append(atributo)
        return lista_atributos


class Financiera:

    def __init__(self, nombre, saldo_institucional):
        self.id = uuid4()
        self.nombre = nombre
        self.saldo_institucional = saldo_institucional
        self.clientes = list()
        self.sumatoria_lineas_credito = 0

    def agregar_cliente(self, cliente):
        if self.sumatoria_lineas_credito <= 0.1*self.saldo_institucional: 
            cliente.financiera = self.nombre
            cliente.linea_credito = 1000000
            self.sumatoria_lineas_credito += 1000000
            self.clientes.append(cliente)
            return self.clientes

        else:
            raise Exception("Lo Lamentamos, no hay capacidad de asignar lineas de crédito!")
            
    
    def eliminar_cliente(self, id_cliente):
        for index, cliente in enumerate(self.clientes):
            if cliente.id == id_cliente:
                delattr(cliente, "financiera")
                delattr(cliente, "linea_credito")
                self.clientes.pop(index)
                return self.clientes
    
    def transferir(self, id_origen, id_destino, monto):
        # revisamos si financiera es origen o destino
        if id_origen == self.id:
            origen = self
        elif id_destino == self.id:
            destino = self

        # como financiera no es origen ni destino entonce
        # se revisa si ambos son clientes
        cliente_origen_encontrado = False
        cliente_destino_encontrado = False
        for cliente in self.clientes:
            if cliente.id == id_origen:
                origen = cliente
                cliente_origen_encontrado = True
            elif cliente.id == id_destino:
                destino = cliente
                cliente_destino_encontrado = True
        if (cliente_destino_encontrado == True
            and cliente_origen_encontrado == False
            and origen != self):
            raise Exception("El origen no se encontró!")
        elif (cliente_destino_encontrado == False 
            and cliente_origen_encontrado == True
            and destino != self):
            raise Exception("El destino no se encontró!")
        if (cliente_destino_encontrado == False 
            and cliente_origen_encontrado == False):
            raise Exception("El origen y el destino no fueron econtrados!")
        else:
            if isinstance(origen, Cliente):
                if (origen.saldo + origen.linea_credito) >= monto:
                    if isinstance(destino, Cliente):
                        destino.saldo += monto
                    elif isinstance(destino, Financiera): 
                        destino.saldo_institucional += monto
                    origen.saldo -= monto
                else:
                    raise Exception("El cliente de origen no tiene saldo suficiente!")
            else:
                if (origen.saldo_institucional-monto)*.1 >= self.sumatoria_lineas_credito:
                    destino.saldo += monto
                    origen.saldo_institucional -= monto
                else:
                    raise Exception("La financiera de origen no tiene saldo suficiente!")

        
    def giros_totales(self):
        pass


if __name__ == "__main__":
    financiera_1 = Financiera("Saka Lukas", 100000000)
    financiera_2 = Financiera("Banco de Talca", 100000000)
    cliente_1 = Cliente("Wolverine", 500000)
    cliente_2 = Cliente("Ciclope", 400000)
    cliente_3 = Cliente("Snoopy", 300000)
    cliente_4 = Cliente("Perro Chocolo", 600000)
    cliente_5 = Cliente("Vaca Loca", 100000)
    cliente_6 = Cliente("Perro Firulais", 200000)
    cliente_7 = Cliente("Chupacabras", 100000)
    cliente_8 = Cliente("Baby Yoda", 700000)
    clientes_grupo_a = [cliente_1, cliente_2, cliente_3, cliente_4]
    clientes_grupo_b = [cliente_5, cliente_6, cliente_7, cliente_8]

    for cliente in clientes_grupo_a:
        financiera_1.agregar_cliente(cliente)

    for cliente in clientes_grupo_b:
        financiera_2.agregar_cliente(cliente)


    def imprimir_clientes():
        for cliente in financiera_1.clientes:
            print(cliente.nombre, "\n", cliente.id, cliente.saldo)

        for cliente in financiera_2.clientes:
            print(cliente.nombre, "\n", cliente.id, cliente.saldo)

    imprimir_clientes()
  
    print("Sumatoria LC", financiera_1.sumatoria_lineas_credito)
    financiera_1.transferir(financiera_1.id, cliente_2.id, 60000000)
    print()
    imprimir_clientes()


    print(cliente_1.atributos)


    # Prueba de eliminación de cliente desde financiera
    # Pierde nombre financiera y linea_credito
    print("\n\n==> PROBANDO ELIMINACIÓN DE CLIENTE")
    print("\nAtributos del cliente_1 antes de ser eliminado")
    print("Ojo existen linea_credito y financiera pues aún pertenece a financiera")
    print(cliente_1.atributos)

    financiera_1.eliminar_cliente(cliente_1.id)

    print("\n\nAtributos del cliente_1 después de ser eliminado")
    print("ya no existen linea_credito y financiera pues aún pertenece a financiera")
    print(cliente_1.atributos)