from lxml import etree
prueba=etree.parse("lol.xml")

from func import listar_nomtil

while True:
    print("Menú de ejercicios")
    print("   1.Listar el titulo y el nombre de todos los campeones")
    print("   2.Contar el numero de campeones")
    print("   3.Lista los campeones que pertenezcan a un rol concreto")
    print("   4.Pedir el rango de ataque y mostrar los campeones que tengan ese rango o superior")
    print("   5.Listar las habilidades que tiene un campeon y el coste de ellas")
    print("   0.Salir")
    # ingresar una opcion
    opcion = int(input("Elija una opción (0-5): "))

    if opcion==1:
    	for nombre,titulo in listar_nomtil(prueba):
    		print(nombre,titulo)