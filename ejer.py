from lxml import etree
prueba=etree.parse("lol.xml")

from func import listar_nomtil,contar_camp,rol_camp,rang_camp

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

    elif opcion==2:
    	print("Hay",contar_camp(prueba),"campeones en el documento")

    elif opcion==3:
    	rol=input("Dime el rol a buscar:")
    	if rol not in rol_camp(prueba,rol):
    		print("Ese rol no existe")
    	for campeones in rol_camp(prueba,rol):
    		print(campeones)

    elif opcion==4:
    	rango=int(input("Dime el rango de ataque:"))
    	if rango <0:
    		print("Error,eso no es posible")
    	else:
    		for campeones in rang_camp(prueba,rango):
    			print(campeones)

    