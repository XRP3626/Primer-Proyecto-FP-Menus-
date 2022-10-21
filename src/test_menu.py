from src.menu import menu
if name =="__main__":
   print("\nTest de la función Menu")
   lista = menu("data/menu.csv")
   print("\Numero total de menus:", len(lista))
   print("\tEstos son los 10 primeros menus")
   print(lista[:10], "\n")