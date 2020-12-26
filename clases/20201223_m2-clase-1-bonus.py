from uuid import uuid4

class Cliente:

    def __init__(self, nombre, saldo):
        self.__id = uuid4()
        self.__nombre = nombre
        self.__saldo = saldo
        self.__atributos = []
    
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
        self.__id = uuid4()
        self.__nombre = nombre
        self.__saldo_institucional = saldo_institucional
        self.__clientes = list()
        self.__sumatoria_lineas_credito = 0

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def saldo_institucional(self):
        return self.__saldo_institucional

    @property
    def clientes(self):
        return self.__clientes

    @property
    def sumatoria_lineas_credito(self):
        return self.__sumatoria_lineas_credito

    def agregar_cliente(self, cliente):
        if self.__sumatoria_lineas_credito <= 0.1*self.__saldo_institucional: 
            cliente.financiera = self.__nombre 
            cliente.linea_credito = 1000000
            self.__sumatoria_lineas_credito += 1000000
            self.__clientes.append(cliente)
            return self.__clientes

        else:
            raise Exception("Error:No hay capacidad para lineas de crédito!")
            
    
    def eliminar_cliente(self, id_cliente):
        for index, cliente in enumerate(self.__clientes):
            if cliente.id == id_cliente:
                delattr(cliente, "financiera")
                delattr(cliente, "linea_credito")
                self.__clientes.pop(index)
                return self.__clientes
    
    def transferir(self, id_origen, id_destino, monto):
        # revisamos si financiera es origen o destino
        if id_origen == self.__id:
            origen = self
        elif id_destino == self.__id:
            destino = self

        # como financiera no es origen ni destino entonce
        # se revisa si ambos son clientes
        cliente_origen_encontrado = False
        cliente_destino_encontrado = False
        for cliente in self.__clientes:
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
                        destino.__saldo_institucional += monto
                    origen.saldo -= monto
                else:
                    raise Exception("Cliente origen con saldo insuficiente!")
            else:
                if ((origen.__saldo_institucional-monto)*.1 
                            >= self.__sumatoria_lineas_credito):
                    destino.saldo += monto
                    origen.__saldo_institucional -= monto
                else:
                    message = "Financiera de origen con saldo insuficiente!"
                    raise Exception(message)
        
    def giros_totales(self):
        pass

    def resumen_clientes(self):
        '''
        Imprime lista de clientes de financiera
        con nombre, id parcial y saldo
        '''
        lista_datos_clientes = list()
        for cliente in self.clientes:
            lista_datos_clientes.append([str(cliente.id)[:5], 
                                cliente.saldo, 
                                cliente.nombre])
        return lista_datos_clientes

    def maximo_transferible(self):
        maximo_monto_transferible = (self.__saldo_institucional 
                - self.__sumatoria_lineas_credito/0.1)
        return maximo_monto_transferible

if __name__ == "__main__":

    # Se instancian 2 financieras
    financiera_1 = Financiera("Saka Lukas", 100000000)
    financiera_2 = Financiera("Banco de Talca", 100000000)

    # Se instancian 8 clientes
    cliente_1 = Cliente("Wolverine", 500000)
    cliente_2 = Cliente("Ciclope", 400000)
    cliente_3 = Cliente("Snoopy", 300000)
    cliente_4 = Cliente("Perro Chocolo", 600000)
    cliente_5 = Cliente("Vaca Loca", 100000)
    cliente_6 = Cliente("Perro Firulais", 200000)
    cliente_7 = Cliente("Chupacabras", 100000)
    cliente_8 = Cliente("Baby Yoda", 700000)

    # Se agrupan clientes en listas de 4 unidades
    clientes_grupo_a = [cliente_1, cliente_2, cliente_3, cliente_4]
    clientes_grupo_b = [cliente_5, cliente_6, cliente_7, cliente_8]

    # Se dan de alta los clientes del grupo_a en financiera_1
    for cliente in clientes_grupo_a:
        financiera_1.agregar_cliente(cliente)

    # Se dan de alta los clientes del grupo_b en financiera_2
    for cliente in clientes_grupo_b:
        financiera_2.agregar_cliente(cliente)

    # Se imprime resumen de clientes (id parcial, saldo y nombre) 
    # de financiera_1
    print("\nSaldos de clientes antes de transferencia")
    for cliente in financiera_1.resumen_clientes():
        print(cliente)
  
    # Calcula máximo monto que financiera puede transferir
    maximo_monto_transferible_1 = financiera_1.maximo_transferible()
    print("\nEl máximo monto transferible es: ", maximo_monto_transferible_1)

    # Transfiere el máximo monto transferible de financiera_1
    financiera_1.transferir(financiera_1.id, cliente_2.id, 
            maximo_monto_transferible_1)
 
    print("\nSaldos de clientes antes de transferencia")
    for cliente in financiera_1.resumen_clientes():
        print(cliente)


    # Prueba de eliminación de cliente desde financiera
    # Pierde nombre financiera y linea_credito
    print("\n\nPROBANDO ELIMINACIÓN DE CLIENTE")
    print("\nAtributos del cliente_1 antes de ser eliminado")
    print("Aún están linea_credito y financiera")
    print("pues aún pertenece a financiera")
    print(cliente_1.atributos)

    # Elimina cliente_1 de financiera_1
    financiera_1.eliminar_cliente(cliente_1.id)

    print("\n\nAtributos del cliente_1 después de ser eliminado")
    print("ya no existen linea_credito y financiera pues ya no")
    print("pertenece a financiera")
    print(cliente_1.atributos)