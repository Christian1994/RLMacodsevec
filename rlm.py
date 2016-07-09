
import numpy as np

class RLM:

	coef = []
	def __init__(): pass

	@classmethod
	def clusterVerde(self):

		y = [1, 0.777777778, 0.9, 0.705882353]


		x = [[0, 0, 0, 0],
			 [1, 0.222222222, 0, 0.117647059],
			 [0, 0.777777778, 0.1, 0.117647059],
			 [0, 0, 0.9, 0.058823529],
			 [0, 0, 0, 0.705882353]]
			 

		X = np.column_stack(x+[[1]*len(x[0])])
		self.coef = np.linalg.lstsq(X,y)[0]

		#print self.coef
		#print ""
		#print np.dot(X,coef)

	@classmethod
	def clusterAmarillo(self):

		y = [0.631578947, 0.666666667]


		x = [[0, 0],
			 [0, 0.111111111],
			 [0.157894737, 0],
			 [0.105263158, 0.111111111],
			 [0.105263158, 0],
			 [0.631578947, 0.111111111],
			 [0, 0.666666667]]
			 
		X = np.column_stack(x+[[1]*len(x[0])])
		self.coef = np.linalg.lstsq(X,y)[0]

		#print self.coef
		#print ""
		#print np.dot(X,coef)

	@classmethod
	def clusterAzul(self):

		y = [0.8125, 0.454545455, 0.454545455, 0.518518519]


		x = [[0, 0, 0, 0.074074074],
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

		X = np.column_stack(x+[[1]*len(x[0])])
		self.coef = np.linalg.lstsq(X,y)[0]

		#print self.coef
		#print ""
		#print np.dot(X,coef)

	@classmethod
	def ecuacionClusterVerde(self, x1, x2, x3, x4, x5):

		self.clusterVerde()

		# Ecuacion de la recta cluster verde
		print ""
		print "Cluster Verde: "
		print "Y = " + str(self.coef[5]) + " + (" + str(self.coef[0]) + ")X1 + (" + str(self.coef[1]) + ")X2 + (" + str(self.coef[2]) + ")X3 + (" + str(self.coef[3]) + ")X4 + (" + str(self.coef[4]) + ")X5"
		print ""

		# Ecuacion de la recta cluster verde
		# return self.coef
		evaluacion = self.coef[5] + self.coef[0]*(float(x1)/float(8)) + self.coef[1]*(float(x2)/float(10)) + self.coef[2]*(float(x3)/float(9)) + self.coef[3]*(float(x4)/float(10)) + self.coef[4]*(float(x5)/float(17))
		return evaluacion

	@classmethod
	def ecuacionClusterAmarillo(self, x1, x2, x3, x4, x5, x6, x7):
		
		self.clusterAmarillo()
		
		# Ecuacion de la recta cluster amarillo
		print ""
		print "Cluster Amarillo: "
		print "Y = " + str(self.coef[7]) + " + (" + str(self.coef[0]) + ")X1 + (" + str(self.coef[1]) + ")X2 + (" + str(self.coef[2]) + ")X3 + (" + str(self.coef[3]) + ")X4 + (" + str(self.coef[4]) + ")X5 + (" + str(self.coef[5]) + ")X6 + (" + str(self.coef[6]) + ")X7"
		print ""

		# Ecuacion de la recta cluster verde
		# return self.coef
		evaluacion = self.coef[7] + self.coef[0]*(float(x1)/float(8)) + self.coef[1]*(float(x2)/float(10)) + self.coef[2]*(float(x3)/float(9)) + self.coef[3]*(float(x4)/float(10)) + self.coef[4]*(float(x5)/float(17)) + self.coef[5]*(float(x6)/float(19)) + self.coef[6]*(float(x7)/float(9))
		return evaluacion

	@classmethod
	def ecuacionClusterAzul(self, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11):

		self.clusterAzul()

		# Ecuacion de la recta cluster azul

		print ""
		print "Cluster Azul: "
		print "Y = " + str(self.coef[11]) + " + (" + str(self.coef[0]) + ")X1 + (" + str(self.coef[1]) + ")X2 + (" + str(self.coef[2]) + ")X3 + (" + str(self.coef[3]) + ")X4 + (" + str(self.coef[4]) + ")X5 + (" + str(self.coef[5]) + ")X6 + (" + str(self.coef[6]) + ")X7 + (" + str(self.coef[7]) + ")X8 + (" + str(self.coef[8]) + ")X9 + (" + str(self.coef[9]) + ")X10 + (" + str(self.coef[10]) + ")X11" 
		print ""

		# Ecuacion de la recta cluster verde
		#return self.coef
		evaluacion = self.coef[11] + self.coef[0]*(float(x1)/float(8)) + self.coef[1]*(float(x2)/float(10)) + self.coef[2]*(float(x3)/float(9)) + self.coef[3]*(float(x4)/float(10)) + self.coef[4]*(float(x5)/float(17)) + self.coef[5]*(float(x6)/float(19)) + self.coef[6]*(float(x7)/float(9)) + self.coef[7]*(float(x8)/float(16)) + self.coef[8]*(float(x9)/float(11)) + self.coef[9]*(float(x10)/float(11)) + self.coef[10]*(float(x11)/float(27))
		return evaluacion

"""
verde = RLM()
verde.clusterVerde()

amarillo = RLM()
amarillo.clusterAmarillo()

azul = RLM()
azul.clusterAzul()
"""