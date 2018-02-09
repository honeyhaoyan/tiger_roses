import numpy as np
import pickle
import csv

data_file = '../data.csv'

X = []
with open(data_file, 'rb') as f:
	csv_reader = csv.DictReader(f)
	for row in csv_reader:
		X.append([row['MSN'], row['StateCode'], int(row['Year']), float(row['Data'])])

with open('../data.pk1', 'wb') as f:
	pickle.dump(X, f)

descriptions = np.array(X)
print (descriptions[:,2])
