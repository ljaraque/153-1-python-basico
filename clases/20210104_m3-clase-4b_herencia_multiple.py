#!/usr/bin/env python
# coding: utf-8

# In[80]:


def imprimir_datos_objeto(objeto):
    nombre_objeto = [ k for k,v in locals().items() if v == objeto][0]
    print("\n"+79*"#")
    print("#### MRO OBJETO")
    print("#### C3 Linearization")
    print("#### Clases hijas se chequean antes que las madres")
    print("#### Madres múltiples se chequean en el orden listado")
    for element in reversed(objeto.__class__.__mro__):
        print(element)
    print("\n#### dir del objeto\n")
    print(dir(objeto))
    print("\n#### Variables de Clase".upper()) 

    for elemento in dir(objeto.__class__):
        if callable(eval(nombre_objeto+"."+elemento)) != True and elemento[:2]!="__":
            print(elemento+":", eval(nombre_objeto+".__class__."+elemento))
    '''
    print("\n#### Métodos de Clase".upper()) 
    for elemento in dir(objeto.__class__):
        if callable(eval(nombre_objeto+"." + elemento)) == True and elemento[:2]!="__":
            print(elemento)
    '''
    print("\n#### Variables de Instancia".upper())
    for clave, valor in vars(objeto).items():
        print(clave+": "+str(valor))

    print("\n#### Métodos de Instancia".upper())
    index=1
    for elemento in dir(objeto):
        if callable(eval(nombre_objeto+"." + elemento)) == True and elemento[:2]=="__":
            if (index)%7==0:
                end_char = "\n"
                index = 0
            else:
                end_char = ","
            print(elemento, end=end_char)
            index +=1
        elif callable(eval(nombre_objeto+"." + elemento)) == True and elemento[:2]!="__":
            try:
                print("\n",elemento, sep="")
                eval(nombre_objeto+"." + elemento+"()")
                index +=1
            except Exception as e:
                print("No se puede evaluar el método " + elemento+"() pues no se ingresaron argumentos")

    print("\n"+79*"#"+"\n")


# In[75]:


class SerVivo00:
    variable_prueba = "viariable_prueba desde SerVivo00"
    variable_prueba_00 = "variable_prueba_00 desde SerVivo00"
    
    def __init__(self):
        print("Ejecutado __init__() de SerVivo00")
        self.variable_prueba = "variable_prueba desde init SerVivo00"
        self.peso = "40 desde init SerVivo00"

    def metodo_prueba(self):
        print("metodo_prueba() desde SerVivo00")
        
    def metodo_prueba00(self):
        print("metodo_prueba00() desde SerVivo00")
        


# In[76]:


class SerVivo01(SerVivo00):
    
    def __init__(self):
        #SerVivo00.__init__(self)
        super().__init__()
        print("Ejecutado __init__() de SerVivo01")
        self.variable_prueba = "variable_prueba desde init SerVivo01"
        self.variable_prueba_01 = "variable_prueba_01 desde init SerVivo01"
        
    def metodo_prueba(self):
        print("metodo_prueba() desde SerVivo01")
        
    def metodo_prueba01(self):
        print("metodo_prueba00() desde SerVivo01")


# In[77]:


servivo_01 = SerVivo01()


# In[78]:


print(servivo_01.variable_prueba)
print(servivo_01.peso)
print(servivo_01.variable_prueba_00)
print(servivo_01.variable_prueba_01)
servivo_01.metodo_prueba()
servivo_01.metodo_prueba00()
servivo_01.metodo_prueba01()


# In[81]:


print(dir(servivo_01))


# In[82]:


imprimir_datos_objeto(servivo_01)


# In[83]:


class SerVivo01b(SerVivo00):
    variable_prueba = "variable_prueba desde clase SerVivo01b"
    variable_prueba_01b = "variable_prueba_01b desde clase SerVivo01b"
    
    def __init__(self):
        super().__init__()
        #SerVivo01.__init__(self)
        self.variable_prueba = "variable_prueba desde init SerVivo01b"
        self.variable_prueba_01b = "variable_prueba_01 desde init SerVivo01b"
        print("Ejecutado __init__() de SerVivo01b")

    def metodo_prueba01(self):
        print("metodo_prueba01b() desde SerVivo01b")
        
    def metodo_prueba(self):
        print("metodo_prueba() desde SerVivo01b")


# In[84]:


servivo_01b = SerVivo01b()


# In[85]:


imprimir_datos_objeto(servivo_01b)


# In[88]:


class SerVivo00Mutacion01(SerVivo01):
    variable_prueba = "variable_prueba desde clase SerVivo00Mutacion01"
    variable_prueba_00Mutacion01 = "variable_prueba_00Mutacion01 desde clase SerVivo00Mutacion01"
    
    def __init__(self):
        print("Ejecutado __init__() de SerVivo00Mutacion01")
        super().__init__()
        #SerVivo01.__init__(self)
        self.variable_prueba = "variable_prueba desde init SerVivo00Mutacion01"
        self.variable_prueba_00Mutacion01 = "variable_prueba_01 desde init SerVivo00Mutacion01"

        
    def metodo_prueba00Mutacion01(self):
        print("metodo_prueba00Mutacion01() desde SerVivo00Mutacion01")
        
    def metodo_prueba(self):
        print("metodo_prueba() desde SerVivo00Mutacion01")


# In[89]:


servivo_00mutacion01= SerVivo00Mutacion01()


# In[90]:


imprimir_datos_objeto(servivo_00mutacion01)


# In[96]:


class SerVivo00Mutacion02(SerVivo01b):
    variable_prueba = "variable_prueba desde clase SerVivo00Mutacion02"
    variable_prueba_00Mutacion02 = "variable_prueba_00Mutacion02 desde clase SerVivo00Mutacion02"
    
    def __init__(self):
        print("Ejecutado __init__() de SerVivo00Mutacion02")
        super().__init__()
        #SerVivo01.__init__(self)
        #self.variable_prueba = "variable_prueba desde init SerVivo00Mutacion02"
        self.variable_prueba_00Mutacion02 = "variable_prueba_00Mutacion02 desde init SerVivo00Mutacion02"
        
        
    def metodo_prueba00Mutacion02(self):
        print("metodo_prueba00Mutacion02() desde SerVivo00Mutacion02")
        
    def metodo_prueba(self):
        print("metodo_prueba() desde SerVivo00Mutacion02")


# In[97]:


servivo_00mutacion02= SerVivo00Mutacion02()


# In[98]:


imprimir_datos_objeto(servivo_00mutacion02)


# In[104]:


class SerVivo02(SerVivo00Mutacion01, SerVivo00Mutacion02):
    #variable_prueba = "variable_prueba desde clase SerVivo02"
    variable_prueba_02 = "variable_prueba_02 desde clase SerVivo02"
    
    def __init__(self):
        print("Ejecutado __init__() de SerVivo02")
        super().__init__()
        #SerVivo00Mutacion02.__init__(self)
        #SerVivo00Mutacion01.__init__(self)
        self.volumen = 40
        
        
    def metodo_prueba02(self):
        print("metodo_prueba02() desde SerVivo02")
        
    #def metodo_prueba(self):
    #    print("metodo_prueba() desde SerVivo02")


# In[105]:


servivo02 = SerVivo02()


# In[106]:


imprimir_datos_objeto(servivo02)

