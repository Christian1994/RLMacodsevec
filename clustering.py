import rlm

class Clustering:

	global objRegresionLinealMultiple
	objRegresionLinealMultiple = rlm.RLM

	# Conjuntos de sintomas
	x1 = 0.0
	x2 = 0.0
	x3 = 0.0 
	x4 = 0.0
	x5 = 0.0
	x6 = 0.0
	x7 = 0.0
	x8 = 0.0
	x9 = 0.0 
	x10 = 0.0 
	x11 = 0.0
	x12 = 0.0

	# Conjuntos de enfermedades
	a1 = 0.0
	a2 = 0.0
	a3 = 0.0
	a4 = 0.0
	a5 = 0.0
	a6 = 0.0
	a7 = 0.0
	a8 = 0.0
	a9 = 0.0
	a10 = 0.0
	a11 = 0.0
	a12 = 0.0

	# Grupos clustering
	g1 = 0.0
	g2 = 0.0 
	g3 = 0.0
	g4 = 0.0 
	g5 = 0.0

	def __init__(): pass

	# Getters de Xi

	@classmethod
	def getX1(self):
		return self.x1

	@classmethod
	def getX2(self):
		return self.x2

	@classmethod
	def getX3(self):
		return self.x3

	@classmethod
	def getX4(self):
		return self.x4

	@classmethod
	def getX5(self):
		return self.x5

	@classmethod
	def getX6(self):
		return self.x6

	@classmethod
	def getX7(self):
		return self.x7

	@classmethod
	def getX8(self):
		return self.x8

	@classmethod
	def getX9(self):
		return self.x9

	@classmethod
	def getX10(self):
		return self.x10

	@classmethod
	def getX11(self):
		return self.x11

	@classmethod
	def getX12(self):
		return self.x12

	# Setters de Xi

	@classmethod
	def setX1(self, x1):
		self.x1 = x1

	@classmethod
	def setX2(self, x2):
		self.x2 = x2

	@classmethod
	def setX3(self, x3):
		self.x3 = x3

	@classmethod
	def setX4(self, x4):
		self.x4 = x4

	@classmethod
	def setX5(self, x5):
		self.x5 = x5

	@classmethod
	def setX6(self, x6):
		self.x6 = x6

	@classmethod
	def setX7(self, x7):
		self.x7 = x7

	@classmethod
	def setX8(self, x8):
		self.x8 = x8

	@classmethod
	def setX9(self, x9):
		self.x9 = x9

	@classmethod
	def setX10(self, x10):
		self.x10 = x10

	@classmethod
	def setX11(self, x11):
		self.x11 = x11

	@classmethod
	def setX12(self, x12):
		self.x12 = x12		

	# Getters de Ai

	@classmethod
	def getA1(self):
		return self.a1

	@classmethod
	def getA2(self):
		return self.a2

	@classmethod
	def getA3(self):
		return self.a3

	@classmethod
	def getA4(self):
		return self.a4

	@classmethod
	def getA5(self):
		return self.a5

	@classmethod
	def getA6(self):
		return self.a6

	@classmethod
	def getA7(self):
		return self.a7

	@classmethod
	def getA8(self):
		return self.a8

	@classmethod
	def getA9(self):
		return self.a9

	@classmethod
	def getA10(self):
		return self.a10

	@classmethod
	def getA11(self):
		return self.a11

	@classmethod
	def getA12(self):
		return self.a12

	# Setters de Ai

	# Acariasis
	@classmethod
	def setA1(self):
		y1 = self.x1;
		if (y1 > 8): y1 = 8
		self.a1 = (y1*float(1)/float(8)) * (float(1)/float(1))

	# Babesiosis
	@classmethod
	def setA2(self):
		y2 = self.x2
		if(y2 > 10): y2 = 10
		self.a2 = (y2*(float(1)/float(10))) * (float(1)/float(1))

	# Coccidiosis
	@classmethod
	def setA3(self):
		y2 = self.x2
		y3 = self.x3
		if(y2 > 2): y2 = 2
		if(y3 > 7): y3 = 7
		self.a3 = (y2*(float(1)/float(2)) + y3*(float(1)/float(7))) * (float(1)/float(2))

	# Dirofilariasis
	@classmethod
	def setA4(self):
		y3 = self.x3
		y4 = self.x4
		if(y3 > 1): y3 = 1
		if(y4 > 9): y4 = 9
		self.a4 = (y3*(float(1)/float(1)) + y4*(float(1)/float(9))) * (float(1)/float(2))

	# Leptospirosis
	@classmethod
	def setA5(self):
		y2 = self.x2
		y3 = self.x3
		y4 = self.x4
		y5 = self.x5
		if(y2 > 2): y2 = 2
		if(y3 > 2): y3 = 2
		if(y4 > 1): y4 = 1
		if(y5 > 12): y5 = 12
		self.a5 = (y2*(float(1)/float(2)) + y3*(float(1)/float(2)) + y4*(float(1)/float(1)) + y5*(float(1)/float(12))) * (float(1)/float(4))

	# Moquillo
	@classmethod
	def setA6(self):
		y3 = self.x3
		y4 = self.x4
		y5 = self.x5
		y6 = self.x6
		if(y3 > 3): y3 = 3
		if(y4 > 2): y4 = 2
		if(y5 > 2): y5 = 2
		if(y6 > 12): y6 =12
		self.a6 = (y3*(float(1)/float(3)) + y4*(float(1)/float(2)) + y5*(float(1)/float(2)) + y6*(float(1)/float(12))) * (float(1)/float(4))

	# Rabia
	@classmethod
	def setA7(self):
		y2 = self.x2
		y4 = self.x4
		y6 = self.x6
		y7 = self.x7
		if(y2 > 1): y2 = 1
		if(y4 > 1): y4 = 1
		if(y6 > 1): y6 = 1
		if(y7 > 6): y7 = 6
		self.a7 = (y2*(float(1)/float(1)) + y4*(float(1)/float(1)) + y6*(float(1)/float(1)) + y7*(float(1)/float(6))) * (float(1)/float(4))

	# Erlichiosis
	@classmethod
	def setA8(self):
		y2 = self.x2
		y3 = self.x3
		y8 = self.x8
		if(y2 > 2): y2 = 2
		if(y3 > 1): y3 = 1
		if(y8 > 13): y8 = 13
		self.a8 = (y2*(float(1)/float(2)) + y3*(float(1)/float(1)) + y8*(float(1)/float(13))) * (float(1)/float(3))

	# Giardiasis
	@classmethod
	def setA9(self):
		y2 = self.x2
		y3 = self.x3
		y6 = self.x6;
		y9 = self.x9;
		if(y2>2): y2 = 2
		if(y3>3): y3 = 3
		if(y6>1): y6 = 1
		if(y9>5): y9 = 5
		self.a9 = (y2*(float(1)/float(2)) + y3*(float(1)/float(3)) + y6*(float(1)/float(1)) + y9*(float(1)/float(5))) * (float(1)/float(4))

	# Parvovirosis
	@classmethod
	def setA10(self):
		y2 = self.x2
		y3 = self.x3
		y6 = self.x6
		y8 = self.x8
		y10 = self.x10
		if(y2>2): y2 = 2
		if(y3>2): y3 = 2
		if(y6>1): y6 = 1
		if(y8>1): y8 = 1
		if(y10>5): y10 = 5
		self.a10 = (y2*(float(1)/float(2)) + y3*(float(1)/float(2)) + y6*(float(1)/float(1)) + y8*(float(1)/float(1)) + y10*(float(1)/float(5))) * (float(1)/float(5))

	# Leishmaniasis
	@classmethod
	def setA11(self):
		y1 = self.x1;
		y3 = self.x3;
		y5 = self.x5;
		y6 = self.x6;
		y8 = self.x8;
		y10 = self.x10;
		y11 = self.x11;
		if(y1 > 2): y1 = 2
		if(y3 > 1): y3 = 1
		if(y5 > 4): y5 = 4
		if(y6 > 2): y6 = 2
		if(y8 > 3): y8 = 3
		if(y10 > 1): y10 = 1
		if(y11 > 14): y11 = 14
		self.a11 = (y1*(float(1)/float(2)) + y3*(float(1)/float(1)) + y5*(float(1)/float(4)) + y6*(float(1)/float(2)) + y8*(float(1)/float(3)) + y10*(float(1)/float(1)) + y11*(float(1)/float(14))) * (float(1)/float(7))

	# Otitis por Otodectes
	@classmethod
	def setA12(self):
		y12 = self.x12
		if(y12 > 6): y12 = 6
		self.a12 = (y12*(float(1)/float(6))) *(float(1)/float(1))	
	
	@classmethod
	def asignar_valores_Ai(self):
		self.setA1()
		self.setA2()
		self.setA3()
		self.setA4()
		self.setA5()
		self.setA6()
		self.setA7()
		self.setA8()
		self.setA9()
		self.setA10()
		self.setA11()
		self.setA12()
	
	@classmethod
	def asignar_valores_Gi(self):
		self.g1 = (self.a1) * (float(1)/float(1))
		self.g2 = (self.a2 + self.a3 + self.a4 + self.a5) * (float(1)/float(4))
		self.g3 = (self.a6 + self.a7) * (float(1)/float(2))
		self.g4 = (self.a8 + self.a9 + self.a10 + self.a11) * (float(1)/float(4))
		self.g5 = (self.a12) * (float(1)/float(1))

	@classmethod
	def mayor_Gi(self):
		salida = "\nMayor Gi ->  "
		if(self.g1 > self.g2 and 
			self.g1 > self.g3 and 
			self.g1 > self.g4 and 
			self.g1 > self.g5):
			salida += "G1: " + str(self.g1) + "\n"
		
		if(self.g2 > self.g1 and 
			self.g2 > self.g3 and 
			self.g2 > self.g4 and 
			self.g2 > self.g5):
			salida += "G2: " + str(self.g2) + "\n"
			print objRegresionLinealMultiple.ecuacionClusterVerde(self.getX1(), self.getX2(), self.getX3(), self.getX4(), self.getX5())

		if(self.g3 > self.g1 and 
			self.g3 > self.g2 and 
			self.g3 > self.g4 and 
			self.g3 > self.g5):
			salida += "G3: " + str(self.g3) + "\n"
			print objRegresionLinealMultiple.ecuacionClusterAmarillo(self.getX1(), self.getX2(), self.getX3(), self.getX4(), self.getX5(), self.getX6(), self.getX7())
		
		if(self.g4 > self.g1 and 
			self.g4 > self.g2 and 
			self.g4 > self.g3 and 
			self.g4 > self.g5):
			salida += "G4: " + str(self.g4) + "\n"
			print objRegresionLinealMultiple.ecuacionClusterAzul(self.getX1(), self.getX2(), self.getX3(), self.getX4(), self.getX5(), self.getX6(), self.getX7(), self.getX8(), self.getX9(), self.getX10(), self.getX11())
		
		if(self.g5 > self.g1 and 
			self.g5 > self.g2 and 
			self.g5 > self.g3 and 
			self.g5 > self.g4):
			salida += "G5: " + str(self.g5) + "\n"
		
		return salida

	@classmethod
	def valoresGi(self):
		salida = ""
		salida = "G1: " + str(self.g1) + "\nG2: " + str(self.g2) + "\nG3: " + str(self.g3) + "\nG4: " + str(self.g4) + "\nG5: " + str(self.g5) + "\n "
		return salida
