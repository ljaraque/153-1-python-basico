import requests
import bs4
import paquete_cientifico as pc

resp = requests.get("https://www.cfg.com")

print(resp.headers)

a=0
b=1
print(a + b)
print("Hemos terminado nuestras actividades Hacker")

print(pc.multiplicar(300, 20))
print(pc.C)
print(pc.PI)
print(pc.vol_cilindro(40, 60))