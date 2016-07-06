
import numpy as np

class rlm:

	def clusterVerde(self):

		y = [1, 0.777777778, 0.9, 0.705882353]


		x = [[0, 0, 0, 0],
			 [1, 0.222222222, 0, 0.117647059],
			 [0, 0.777777778, 0.1, 0.117647059],
			 [0, 0, 0.9, 0.058823529],
			 [0, 0, 0, 0.705882353]]
			 

		X = np.column_stack(x+[[1]*len(x[0])])
		coef = np.linalg.lstsq(X,y)[0]

		print coef
		print ""
		print np.dot(X,coef)

		# Ecuacion de la recta cluster verde

		print ""
		print "Cluster Verde: "
		print "Y = " + str(coef[5]) + " + (" + str(coef[0]) + ")X1 + (" + str(coef[1]) + ")X2 + (" + str(coef[2]) + ")X3 + (" + str(coef[3]) + ")X4 + (" + str(coef[4]) + ")X5"
		print ""

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
		coef = np.linalg.lstsq(X,y)[0]

		print coef
		print ""
		print np.dot(X,coef)

		# Ecuacion de la recta cluster amarillo

		print ""
		print "Cluster Amarillo: "
		print "Y = " + str(coef[7]) + " + (" + str(coef[0]) + ")X1 + (" + str(coef[1]) + ")X2 + (" + str(coef[2]) + ")X3 + (" + str(coef[3]) + ")X4 + (" + str(coef[4]) + ")X5 + (" + str(coef[5]) + ")X6 + (" + str(coef[6]) + ")X7"
		print ""

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
		coef = np.linalg.lstsq(X,y)[0]

		print coef
		print ""
		print np.dot(X,coef)

		# Ecuacion de la recta cluster azul

		print ""
		print "Cluster Azul: "
		print "Y = " + str(coef[11]) + " + (" + str(coef[0]) + ")X1 + (" + str(coef[1]) + ")X2 + (" + str(coef[2]) + ")X3 + (" + str(coef[3]) + ")X4 + (" + str(coef[4]) + ")X5 + (" + str(coef[5]) + ")X6 + (" + str(coef[6]) + ")X7 + (" + str(coef[7]) + ")X8 + (" + str(coef[8]) + ")X9 + (" + str(coef[9]) + ")X10 + (" + str(coef[10]) + ")X11" 
		print ""

verde = rlm()
verde.clusterVerde()

amarillo = rlm()
amarillo.clusterAmarillo()

azul = rlm()
azul.clusterAzul()