
import numpy as np

class RLM:

	x = []
	y = []
	coef = []
	evaluacion = 0.0
	def __init__(): pass

	#-----------------------------------------------------------------------------------------------------------------------------------------------------------
	# Metodos para retornar las matrices X (variables explicativas) y Y (variables respuesta) para la regresion lineal multiple y futuros calculos
	@classmethod
	def matricesXYClusterVerde(self, x, y):

		self.y = [1, 0.777777778, 0.9, 0.705882353]

		self.x = [[0, 0, 0, 0],
				  [1, 0.222222222, 0, 0.117647059],
				  [0, 0.777777778, 0.1, 0.117647059],
				  [0, 0, 0.9, 0.058823529],
				  [0, 0, 0, 0.705882353]]

	@classmethod
	def matricesXYClusterAmarillo(self, x, y):

		self.y = [0.631578947, 0.666666667]

		self.x = [[0, 0],
				  [0, 0.111111111],
				  [0.157894737, 0],
				  [0.105263158, 0.111111111],
				  [0.105263158, 0],
				  [0.631578947, 0.111111111],
				  [0, 0.666666667]]

	@classmethod
	def matricesXYClusterAzul(self, x, y):

		self.y = [0.8125, 0.454545455, 0.454545455, 0.518518519]

		self.x = [[0, 0, 0, 0.074074074],
				  [0.125, 0.181818182, 0.181818182, 0],
				  [0.0625, 0.272727273, 0.181818182, 0.037037037],
				  [0, 0, 0, 0],
				  [0, 0, 0, 0.148148148],
				  [0, 0.090909091, 0.090909091, 0.074074074],
				  [0, 0, 0, 0],
				  [0.8125, 0, 0.090909091, 0.111111111],
				  [0, 0.454545455, 0, 0],
				  [0, 0, 0.454545455, 0.037037037],
				  [0, 0, 0, 0.518518519]]

	#-----------------------------------------------------------------------------------------------------------------------------------------------------------
	# Metodos de regresion lineal multiple de los clusteres verde, amarillo y azul

	@classmethod
	def RLMclusterVerde(self):

		self.matricesXYClusterVerde(self.x, self.y)			 

		X = np.column_stack(self.x+[[1]*len(self.x[0])])
		self.coef = np.linalg.lstsq(X,self.y)[0]

		#print self.coef
		#print ""
		#print np.dot(X,coef)

	@classmethod
	def RLMclusterAmarillo(self):

		self.matricesXYClusterAmarillo(self.x, self.y)
			 
		X = np.column_stack(self.x+[[1]*len(self.x[0])])
		self.coef = np.linalg.lstsq(X,self.y)[0]

		#print self.coef
		#print ""
		#print np.dot(X,coef)

	@classmethod
	def RLMclusterAzul(self):

		self.matricesXYClusterAzul(self.x, self.y)

		X = np.column_stack(self.x+[[1]*len(self.x[0])])
		self.coef = np.linalg.lstsq(X,self.y)[0]

		#print self.coef
		#print ""
		#print np.dot(X,coef)

	#-----------------------------------------------------------------------------------------------------------------------------------------------------------
	# Metodos para evaluar la recta de prediccion de cada cluster

	@classmethod
	def ecuacionClusterVerde(self, x1, x2, x3, x4, x5):

		self.RLMclusterVerde()

		# Ecuacion de la recta cluster verde
		print ""
		print "Cluster Verde: "
		print "Y = " + str(self.coef[5]) + " + (" + str(self.coef[0]) + ")X1 + (" + str(self.coef[1]) + ")X2 + (" + str(self.coef[2]) + ")X3 + (" + str(self.coef[3]) + ")X4 + (" + str(self.coef[4]) + ")X5"
		print ""

		# Ecuacion de la recta cluster verde
		# return self.coef
		self.evaluacion = self.coef[5] + self.coef[0]*(float(x1)/float(8)) + self.coef[1]*(float(x2)/float(10)) + self.coef[2]*(float(x3)/float(9)) + self.coef[3]*(float(x4)/float(10)) + self.coef[4]*(float(x5)/float(17))
		return self.evaluacion

	@classmethod
	def ecuacionClusterAmarillo(self, x1, x2, x3, x4, x5, x6, x7):
		
		self.RLMclusterAmarillo()
		
		# Ecuacion de la recta cluster amarillo
		print ""
		print "Cluster Amarillo: "
		print "Y = " + str(self.coef[7]) + " + (" + str(self.coef[0]) + ")X1 + (" + str(self.coef[1]) + ")X2 + (" + str(self.coef[2]) + ")X3 + (" + str(self.coef[3]) + ")X4 + (" + str(self.coef[4]) + ")X5 + (" + str(self.coef[5]) + ")X6 + (" + str(self.coef[6]) + ")X7"
		print ""

		# Ecuacion de la recta cluster verde
		# return self.coef
		self.evaluacion = self.coef[7] + self.coef[0]*(float(x1)/float(8)) + self.coef[1]*(float(x2)/float(10)) + self.coef[2]*(float(x3)/float(9)) + self.coef[3]*(float(x4)/float(10)) + self.coef[4]*(float(x5)/float(17)) + self.coef[5]*(float(x6)/float(19)) + self.coef[6]*(float(x7)/float(9))
		return self.evaluacion

	@classmethod
	def ecuacionClusterAzul(self, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11):

		self.RLMclusterAzul()

		# Ecuacion de la recta cluster azul

		print ""
		print "Cluster Azul: "
		print "Y = " + str(self.coef[11]) + " + (" + str(self.coef[0]) + ")X1 + (" + str(self.coef[1]) + ")X2 + (" + str(self.coef[2]) + ")X3 + (" + str(self.coef[3]) + ")X4 + (" + str(self.coef[4]) + ")X5 + (" + str(self.coef[5]) + ")X6 + (" + str(self.coef[6]) + ")X7 + (" + str(self.coef[7]) + ")X8 + (" + str(self.coef[8]) + ")X9 + (" + str(self.coef[9]) + ")X10 + (" + str(self.coef[10]) + ")X11" 
		print ""

		# Ecuacion de la recta cluster verde
		#return self.coef
		self.evaluacion = self.coef[11] + self.coef[0]*(float(x1)/float(8)) + self.coef[1]*(float(x2)/float(10)) + self.coef[2]*(float(x3)/float(9)) + self.coef[3]*(float(x4)/float(10)) + self.coef[4]*(float(x5)/float(17)) + self.coef[5]*(float(x6)/float(19)) + self.coef[6]*(float(x7)/float(9)) + self.coef[7]*(float(x8)/float(16)) + self.coef[8]*(float(x9)/float(11)) + self.coef[9]*(float(x10)/float(11)) + self.coef[10]*(float(x11)/float(27))
		return self.evaluacion

	#-----------------------------------------------------------------------------------------------------------------------------------------------------------
	# Metodos para prediccion de enfermedades dentro de cada cluster

	@classmethod
	def prediccionEnfermedadCG(self, evaluacion):

		enfermedades = ["Babesiosis", "Coccidiosis", "Dirofilariasis", "Leptospirosis"]
		y = [1, 0.777777778, 0.9, 0.705882353]		
		yerrabsg = []

		for i in range(len(y)):
			yerrabsg += [abs(y[i] - self.evaluacion)]  

		print yerrabsg

		menor = yerrabsg[0]
		indice = 0
		for i in range(1, len(yerrabsg)):
			if(yerrabsg[i] < menor):
				menor = yerrabsg[i]
				indice = i

		print menor
		print "SCE: " + str(self.SCEclusterVerde(self.y, self.evaluacion))
		return enfermedades[indice]

	@classmethod
	def prediccionEnfermedadCY(self, evaluacion):

		enfermedades = ["Moquillo", "Rabia"]
		y = [0.631578947, 0.666666667] 
		yerrabsy = []

		for i in range(len(y)):
			yerrabsy += [abs(y[i] - self.evaluacion)]

		print yerrabsy

		menor = yerrabsy[0]
		indice = 0
		for i in range(1, len(yerrabsy)):
			if(yerrabsy[i] < menor):
				menor = yerrabsy[i]
				indice = i
				
		print menor
		print "SCE: " + str(self.SCEclusterAmarillo(self.y, self.evaluacion))
		return enfermedades[indice]

	@classmethod
	def prediccionEnfermedadCB(self, evaluacion):

		enfermedades = ["Erlichiosis", "Giardiasis", "Parvovirosis", "Leishmaniasis"]
		y = [0.8125, 0.454545455, 0.454545455, 0.518518519]
		yerrabsb = []

		for i in range(len(y)):
			yerrabsb += [abs(y[i] - self.evaluacion)] # Implementar sumatoria de errores cuadraticos

		print yerrabsb

		menor = yerrabsb[0]
		indice = 0
		for i in range(1, len(yerrabsb)):
			if(yerrabsb[i] < menor):
				menor = yerrabsb[i]
				indice = i

		print menor
		print "SCE: " + str(self.SCEclusterAzul(self.y, self.evaluacion))
		return enfermedades[indice]

	#-----------------------------------------------------------------------------------------------------------------------------------------------------------
	# Metodos para calcular el SCE de cada cluster

	@classmethod
	def SCEclusterVerde(self, y, evaluacion):
		sce = 0.0
		for i in range(len(self.y)):
			sce += ((self.y[i] - self.evaluacion)**2)

		return sce

	@classmethod
	def SCEclusterAmarillo(self, y, evaluacion):
		sce = 0.0
		for i in range(len(self.y)):
			sce += ((self.y[i] - self.evaluacion)**2)

		return sce

	@classmethod
	def SCEclusterAzul(self, y, evaluacion):
		sce = 0.0
		for i in range(len(self.y)):
			sce += ((self.y[i] - self.evaluacion)**2)

		return sce

"""
verde = RLM()
verde.clusterVerde()

amarillo = RLM()
amarillo.clusterAmarillo()

azul = RLM()
azul.clusterAzul()
"""

# Notas importantes:
# Implementar sumatoria de errores cuadraticos SCE (Error en la suma de cuadrados Sumatoria((Y - ^Y) ** 2))
# Tratar de probar la implementacion de regresion cuadratica o exponencial para comparar errores a fin de plantear alternativas
# Matriz de confusion
# Datos de entrada y base de conocimiento dinamicamente mediante carga de archivos de texto
# Mejorar codificacion en cuanto funcione
# Tratar de proponer algoritmo de clustering mediante elemento sobre norma Ai