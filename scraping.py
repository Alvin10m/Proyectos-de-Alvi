import requests
import csv
from bs4 import BeautifulSoup

link = "https://books.toscrape.com/"
respuesta_del_sitio = requests.get(link)
print("Código HTTP:", respuesta_del_sitio.status_code)

soup = BeautifulSoup(respuesta_del_sitio.text, "html.parser")
print("Título de la página:", soup.title.get_text())

# ==Extraer los productos ===
productos = soup.find_all("article", class_="product_pod")
print("Cantidad de productos:", len(productos))

lista_de_productos = []

for producto in productos:
    titulo = producto.h3.a["title"]
    precio = producto.find("p", class_="price_color").get_text()
    link_producto = "https://books.toscrape.com/" + producto.h3.a["href"]
    imagen_producto = "https://books.toscrape.com/" + producto.find("img")["src"]

    lista_de_productos.append({
        "titulo": titulo,
        "precio": precio,
        "url": link_producto,
        "imagen": imagen_producto
    })

# === Guardar en CSV ===
with open("todos_los_libros.csv", "w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Título", "Precio", "URL", "Imagen"])

    for libro in lista_de_productos:
        writer.writerow([libro["titulo"], libro["precio"], libro["url"], libro["imagen"]])
        
ruta_csv = "/home/alvin/Escritorio/todos_los_libros.csv"

with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Título", "Precio", "URL", "Imagen"])

    for libro in lista_de_productos:
        writer.writerow([libro["titulo"], libro["precio"], libro["url"], libro["imagen"]])

print("Scraping completado. Se guardaron:", len(lista_de_productos), "productos.")
print("Archivo creado: todos_los_libros.csv")
