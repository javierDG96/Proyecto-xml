from lxml import etree

def listar_nomtil(prueba):
	nombre=prueba.xpath("//Champion/name/text()")
	titulo=prueba.xpath("//Champion/title/text()")
	return zip(nombre,titulo)

