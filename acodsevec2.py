# Cluster verde

import numpy as np

y = [1, 0.777777778, 0.9, 0.705882353]


x = [[0, 0, 0, 0],
	 [1, 0.222222222, 0, 0.117647059],
	 [0, 0.777777778, 0.1, 0.117647059],
	 [0, 0, 0.9, 0.058823529],
	 [0, 0, 0, 0.705882353]]

# Sumatoria
def sumatoria(array):
	suma = 0
	for i in range(len(array)):
		suma += array[i]
	return suma

# Sumatoria entre elementos de dos arreglos. Implicitamente la sumatoria cuadratica
def sumatelems(a1, a2):
	suma = 0
	for i in range(len(a1)):
		suma += a1[i] * a2[i]
	return suma

def clusterVerde(x, y):

	XTX = [[]]

	print ""
	print "Matriz XTX"
	print ""

	XTX[0] += [len(x[0]), sumatoria(x[0]), sumatoria(x[1]), sumatoria(x[2]), sumatoria(x[3])]
	XTX.append([])
	XTX[1] += [sumatoria(x[0]), sumatelems(x[0], x[0]), sumatelems(x[0], x[1]), sumatelems(x[0], x[2]), sumatelems(x[0], x[3])]
	XTX.append([])
	XTX[2] += [sumatoria(x[1]), sumatelems(x[1], x[0]), sumatelems(x[1], x[1]), sumatelems(x[1], x[2]), sumatelems(x[1], x[3])]
	XTX.append([])
	XTX[3] += [sumatoria(x[2]), sumatelems(x[2], x[0]), sumatelems(x[2], x[1]), sumatelems(x[2], x[2]), sumatelems(x[2], x[3])]
	XTX.append([])
	XTX[4] += [sumatoria(x[3]), sumatelems(x[3], x[0]), sumatelems(x[3], x[1]), sumatelems(x[3], x[2]), sumatelems(x[3], x[3])]


	for i in range(len(XTX)):
		print XTX[i]

	print ""
	print "Matriz XTY"
	print ""

	XTY = []
	XTY += [sumatoria(y), sumatelems(x[0], y), sumatelems(x[1], y), sumatelems(x[2], y), sumatelems(x[3], y)]
	print XTY

	print ""
	print "Matriz Inversa de XTX"
	print ""
	XTXI = np.linalg.inv(XTX)

	for i in range(len(XTXI)):
		print XTXI[i]

	print ""
	print "Coeficientes:"
	print ""
	print np.matmul(XTXI, XTY)

clusterVerde(x, y)