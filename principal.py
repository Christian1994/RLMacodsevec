import clustering

class Principal:

	global objClustering
	objClustering = clustering.Clustering

	def __init__(self, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12):
		objClustering.setX1(x1)
		objClustering.setX2(x2)
		objClustering.setX3(x3)
		objClustering.setX4(x4)
		objClustering.setX5(x5)
		objClustering.setX6(x6)
		objClustering.setX7(x7)
		objClustering.setX8(x8)
		objClustering.setX9(x9)
		objClustering.setX10(x10)
		objClustering.setX11(x11)
		objClustering.setX12(x12)

		objClustering.asignar_valores_Ai()
		objClustering.asignar_valores_Gi()
		resultado = objClustering.mayor_Gi()
		print resultado
		print objClustering.valoresGi()

		print "A1 " + str(objClustering.getA1())
		print "A2 " + str(objClustering.getA2())
		print "A3 " + str(objClustering.getA3())
		print "A4 " + str(objClustering.getA4())
		print "A5 " + str(objClustering.getA5())
		print "A6 " + str(objClustering.getA6())
		print "A7 " + str(objClustering.getA7())
		print "A8 " + str(objClustering.getA8())
		print "A9 " + str(objClustering.getA9())
		print "A10 " + str(objClustering.getA10())
		print "A11 " + str(objClustering.getA11())
		print "A12 " + str(objClustering.getA12())

def main():

	# Pruebas

	# objMain = Principal(0,2,7,0,0,0,0,0,0,0,0,0) # Coccidiosis
	# objMain = Principal(0,0,1,9,0,0,0,0,0,0,0,0) # Dirofilariasis
	# objMain = Principal(0,2,2,1,12,0,0,0,0,0,0,0) # Coccidiosis
	# objMain = Principal(0,0,3,2,2,12,0,0,0,0,0,0) # Moquillo
	# objMain = Principal(0,1,0,1,0,1,6,0,0,0,0,0) # Rabia
	objMain = Principal(0,2,1,0,0,0,0,13,0,0,0,0) # Erlichiosis
	# objMain = Principal(0,2,3,0,0,1,0,0,5,0,0,0) # Giardiasis o Parvovirosis (Factores)
	# objMain = Principal(0,2,2,0,0,1,0,1,0,5,0,0) # Parvovirosis o Giardiasis (Factores)
	# objMain = Principal(2,0,1,0,4,2,0,3,0,1,14,0) # Leishmaniasis

	# objMain = Principal(0,0,0,0,12,0,0,0,0,0,0,0) # Moquillo (?) -> Leptospirosis Porcentajes G muy bajos: El mayor 12.5%. Concentracion de todos los sintomas en un solo Xi
	# objMain = Principal(0,0,0,2,1,2,0,1,0,0,0,0) # Moquillo Porcentaje G mayor a 40% (A considerar, aunque el limite del mayor G sera 0.6 por el momento)
	# objMain = Principal(0,3,3,1,3,0,0,0,0,0,0,0) # Coccidiosis -> Leptospirosis
	# objMain = Principal(2,0,0,0,2,0,0,2,0,0,2,0) # Procentajes G muy bajos: El mayor 25%. Dispersion de los sintomas en sus conjuntos Xi
	# objMain = Principal(0,0,1,1,1,1,0,0,0,0,0,0) # Moquillo Porcentaje G mayor a 40% (A considerar, aunque el limite del mayor G sera 0.6 por el momento)
	# objMain = Principal(0,0,3,0,0,3,1,0,0,0,0,0) # Giardiasis - Parvovirosis Porcentajes G bajos: El mayor aprox. 38%

if __name__ == "__main__":
	main()