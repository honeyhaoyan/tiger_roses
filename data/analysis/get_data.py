from analysis import *
import numpy as np

matrix_path = '../matrix/'

test=get_matrix('Energy type', ['FF','NU','RE','EL','EL'], stable_type=['sector','unit2'], s_type=['TC','B']) +\
	 get_matrix('Energy type', ['FF','NU','RE','EL','EL'], stable_type=['sector','unit2'], s_type=['ET','B']) +\
	 get_matrix('Energy type', ['FF','NU','RE','EL','EL'], stable_type=['sector','unit2'], s_type=['NI','B']) +\
	 get_matrix('Energy type', ['FF','NU','RE','EL','EL'], stable_type=['sector','unit2'], s_type=['IS','B'])
test = test[:,:,:]

print (test)
'''
test=get_matrix('sector',['AC','CC','IC','RC','EI','TX'], stable_type=['Energy type','unit2'], s_type=['TE','V']) - \
	 get_matrix('sector',[',' ,',' ,',' ,',' ,',' ,'AC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) - \
	 get_matrix('sector',[',' ,',' ,',' ,',' ,',' ,'CC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) - \
	 get_matrix('sector',[',' ,',' ,',' ,',' ,',' ,'IC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) - \
	 get_matrix('sector',[',' ,',' ,',' ,',' ,',' ,'RC'], stable_type=['Energy type','unit2'], s_type=['TE','V']) - \
	 get_matrix('sector',[',' ,',' ,',' ,',' ,',' ,'EI'], stable_type=['Energy type','unit2'], s_type=['TE','V'])
matrices = get_matrix('sector', ['A', 'C', 'I', 'R', 'E'],
		stable_type = ['Energy type', 'unit2'],
		s_type = ['TE', 'B'])
for i in range(4):
	print matrices[i][4]
'''
