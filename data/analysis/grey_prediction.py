# GM(1,1)
import numpy as np
from math import exp
from analysis import *

alpha = 0.5
# eps = 1e-10

def pred_of_np(x_0):
	global alpha
	n = len(x_0)
	# print("x_0",x_0)

	x_1 = []
	x_1.append(x_0[0])
	for i in range(1,n):
		x_1.append(x_1[-1]+x_0[i])
	x_1 = np.array(x_1)
	# print("x_1", x_1)

	z_1 = np.array([0])
	z_1 = np.append(z_1, alpha * x_1[1:n] + (1 - alpha) * x_1[0:n-1])
	# print(len(z_1) - len(x_0))

	Y = x_0[1:][:,np.newaxis]
	# print("Y", Y)

	B_1 = (-z_1[1:])[:,np.newaxis]
	B_2 = (np.zeros(n-1) + 1)[:,np.newaxis]
	# print("B_1",B_1)
	# print("B_2",B_2)

	B = np.mat(np.hstack([B_1, B_2]))
	B_t = B.transpose()
	# print("B", B)
	# print("B_t", B_t)
	# print(B_t * B)
	# if(np.linalg.matrix_rank(B_t * B) < 2):
	# 	u = [1e-16,x_0[0]]
	# 	# print("not ")
	# 	# return None
	# else:
	u = (B_t * B).I * B_t * Y
	# print("u", u)
	u = np.array(u).flatten()
	a = u[0]
	b = u[1]

	x_0 = x_0.tolist()
	x_1 = x_1.tolist()
	x_0_pred = [x_0[0]]
	x_1_pred = [x_1[0]]
	# print(a,b)
	# print(b/a)
	for i in range(1, n*2):
		x_1_new = (x_1[0] - b / a) * exp(-a*i) + b / a
		x_0_pred.append(x_1_new - x_1_pred[-1])	
		x_1_pred.append(x_1_new)

	eps = np.array(x_0_pred[0:n]) - np.array(x_0)
	# print(np.array(x_0_pred[0:n]))
	# print(eps)
	s1 = np.var(np.array(x_0_pred[0:n]))
	s2 = np.var(eps)
	print(s1, s2, s2 / s1)
	# print(x_0_pred[0:n])
	return np.array(x_0_pred[n:])

# x_0 = np.array([0,0,0])

# p = pred_of_np(x_0)
# q = np.array([8, 16, 32])
# q = np.array()
# print(p)
# print(q)
# print(p/q)

def prediction(matrix):
	x, y, z = matrix.shape
	for i in range(x):
		for j in range(y):
			matrix[i][j] = pred_of_np(matrix[i][j])
	# print(matrix)
	return matrix

# m = get_matrix('Energy type', ['CL','NN','PM'], stable_type=['sector','unit2'], s_type=['TC','B'])
# # m1 = m[1]
# prediction(m)