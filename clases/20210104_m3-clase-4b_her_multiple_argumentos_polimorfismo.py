#!/usr/bin/env python
# coding: utf-8

# In[41]:


class Animal():
    
    def __init__(self,nombre, peso, posicion):
        self.nombre = nombre
        self.peso = peso
        self.posicion = posicion

    def alimentarse(self, cantidad):
        self.peso += cantidad
        return self.peso
    
    def ejercitar(self, tiempo):
        self.peso -= 0.1 * tiempo # tiempo[s] ==> 0.1 [kg/s]
        return self.peso

    def moverse(self, distancia):
        self.peso -= 0.01*distancia
        self.posicion += distancia
        mensaje = "Me desplacé a la posición "
        return mensaje, self.posicion


# In[43]:


nemo = Animal("Nemo", 1, 0)


# In[44]:


print(nemo.moverse(10))
print(nemo.moverse(-7))


# In[79]:


class AnimalDeCircoChino(Animal):
    
    def __init__(self, nombre, peso, posicion, grupo):
        import time
        self.time = time
        Animal.__init__(self, nombre, peso, posicion)
        self.grupo = grupo

    def moverse(self, energia):
        distancia = 0
        for i in range(energia):
            print("Tomando impulso.. ", end=" ")
            self.time.sleep(0.2)
            distancia += 3
        print()
        mensaje, resultado = Animal.moverse(self, distancia)
        return "Tomando mucho impulso, Salté y "+mensaje, resultado


# In[80]:


animal_de_ciro_chino= AnimalDeCircoChino("chin wen", 20, 0, "Yun Yun")


# In[81]:


animal_de_ciro_chino.moverse(20)


# In[82]:


class Serpiente(Animal):
    
    def __init__(self, nombre, peso, posicion, propietario, grosor_piel, venenosa=True):
        super().__init__(nombre, peso, posicion)
        self.propietario = propietario
        self.grosor_piel = grosor_piel
        self.venenosa = venenosa
    
    def moverse(self, distancia):
        mensaje, resultado = super().moverse(distancia)
        return "Arrastándome " + mensaje + " " + str(resultado)


# In[83]:


piton = Serpiente("pitonisa", 30, 0, "Jonathan", 1, True)


# In[84]:


piton.moverse(20)


# In[89]:


class SerpienteAcrobatica(AnimalDeCircoChino, Serpiente):
    
    def __init__(self, nombre, peso, posicion, propietario, grosor_piel, venenosa, grupo):
        Serpiente.__init__(self, nombre, peso, posicion, propietario, grosor_piel, venenosa)
        AnimalDeCircoChino.__init__(self, nombre, peso, posicion, grupo)


# In[90]:


SerpienteAcrobatica.__mro__


# In[91]:


serpiente_acrobatica = SerpienteAcrobatica("serpentina", 20, 0, "Jonathan", 2, True, "Awakelab")


# In[92]:


serpiente_acrobatica.moverse(30)


# In[93]:


serpiente_acrobatica.propietario


# In[94]:


serpiente_acrobatica.venenosa


# In[95]:


import this

