# Cluster Verde

import numpy as np

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
print "Y = " + str(coef[5]) + " + (" + str(coef[4]) + ")X1 + (" + str(coef[3]) + ")X2 + (" + str(coef[2]) + ")X3 + (" + str(coef[1]) + ")X4 + (" + str(coef[0]) + ")X5"