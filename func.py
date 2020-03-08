from lxml import etree

def listar_nomtil(prueba):
	nombre=prueba.xpath("//Champion/name/text()")
	titulo=prueba.xpath("//Champion/title/text()")
	return zip(nombre,titulo)

def contar_camp(prueba):
	cant=prueba.xpath("//Champion/name/text()")
	return len(cant)

def rol_camp(prueba,rol):
	campeones=[]
	campeones=prueba.xpath('//Champion[tags="%s"]/name/text()' % (rol))
	return campeones

def rang_camp(prueba,rango):
	campeones=prueba.xpath('//Champion/estadisticas[range>="%s"]/../name/text()'%(rango))
	return campeones
	



