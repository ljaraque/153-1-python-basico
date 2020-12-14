import requests
import bs4
import json
import time
import datetime

verduras_lider = requests.get("https://www.lider.cl/supermercado/category/Frutas-y-Verduras/_/N-1vsgxxq")
dom = bs4.BeautifulSoup(verduras_lider.text)
#for elemento in dom.select('span'):

elementos_precios = dom.find_all('span', attrs={'class' : 'price-sell'})
elementos_nombres = dom.find_all('span', attrs={'class' : 'product-name'})

lista_verduras = []
for index, nombre in enumerate(elementos_nombres):
    print(nombre.text, elementos_precios[index].text.strip("$").replace(".",""))
    lista_verduras.append((nombre.text, elementos_precios[index].text.strip("$").replace(".","")))

archivo = open("verduras_"+str(datetime.datetime.now())+".csv", "w")
for verdura_nombre, verdura_precio in lista_verduras:
    archivo.write(verdura_nombre + "," + verdura_precio + "\n")
archivo.close()

'''
while True:
    datos_mindicador = requests.get("https://mindicador.cl/api")
    datos_mindicador_dict = json.loads(datos_mindicador.text)
    print("Dolar: ", datos_mindicador_dict['dolar']['valor'])
    print("UF: ", datos_mindicador_dict['uf']['valor'])
    time.sleep(0.4)

'''