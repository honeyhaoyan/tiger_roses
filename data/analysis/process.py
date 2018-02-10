import numpy as np
import pickle
import csv

data_file = '../msn.csv'

X = []
tags = []
e_type_dict = dict()
s_type_dict = dict()
c_type_dict = dict()
u_type_dict = dict()

'''
e_type_dict["AB"] = "Aviation gasoline blending components"
e_type_dict["AR"] = "Asphalt and road oil"
e_type_dict["AV"] = "Aviation gasoline"
e_type_dict["BM"] = "Biomass"
e_type_dict["CC"] = "Coal coke"
e_type_dict["CL"] = "Coal"
e_type_dict["CO"] = "Crude oil"
e_type_dict["DF"] = "Distillate fuel oil"
e_type_dict["DK"] = "Distillate fuel oil and kerosene-type jet fuel"
e_type_dict["EL"] = "Electricity export/import"
e_type_dict["EM"] = "Fuel ethanol, excluding denaturant,"
e_type_dict["EN"] = "Fuel ethanol, including denaturant"
e_type_dict["ES"] = "Electricity"
e_type_dict["FF"] = "Fossil fuels"
e_type_dict["FN"] = "Petrochemical feedstocks, naphtha less than 401 degrees F"
e_type_dict["FO"] = "Petrochemical feedstocks, other oils equal to or greater than 401 degrees F"
e_type_dict["FS"] = "Petrochemical feedstocks, still gas"
e_type_dict["GD"] = "gross domestic product"
e_type_dict["GE"] = "geothermal energy"
e_type_dict["GO"] = "Geothermal energy and hydroelectricity/Geothermal and solar energy"
e_type_dict["HY"] = "Hydroelectricity"
e_type_dict["JF"] = "Jet fuel"
e_type_dict["JK"] = "Kerosene-type jet fuel"
e_type_dict["JN"] = "Naphtha-type jet fuel"
e_type_dict["KS"] = "Kerosene"
e_type_dict["LG"] = "LPG"
e_type_dict["LO"] = "electrical system energy losses"
e_type_dict["LU"] = "Lubricants"
e_type_dict["MB"] = "Motor gasoline blending components"
e_type_dict["MG"] = "Motor gasoline"
e_type_dict["MM"] = "Motor gasoline excluding fuel ethanol"
e_type_dict["MS"] = "Miscellaneous petroleum products"
e_type_dict["NA"] = "Natural gasoline"
e_type_dict["NG"] = "Natural gas"
e_type_dict["NN"] = "Natural gas (Code used in SEDS 2006.)"
e_type_dict["NU"] = "Electricity produced"
e_type_dict["P1"] = 'Asphalt and road oil, kerosene, lubricants, and "other petroleum products"'
e_type_dict["P5"] = "Other petroleum products (SG and PC consumed as process fuel and AB, MB, PP, and UO consumed as intermediate products)."
e_type_dict["PA"] = "All petroleum products"
e_type_dict["PC"] = "Petroleum coke"
e_type_dict["PE"] = "Primary energy"
e_type_dict["PL"] = "Plant condensate"
e_type_dict["PM"] = "All petroleum products"
e_type_dict["PO"] = "Other petroleum products"
e_type_dict["PP"] = "Pentanes plus"
e_type_dict["RE"] = "Renewable energy"
e_type_dict["RF"] = "Residual fuel oil"
e_type_dict["RO"] = "Renewable energy production, other than fuel ethanol."
e_type_dict["SF"] = "Supplemental gaseous fuels"
e_type_dict["SG"] = "Still gas"
e_type_dict["SN"] = "Special naphthas"
e_type_dict["SO"] = "photovoltaic and solar thermal energy"
e_type_dict["TE"] = "Total energy"
e_type_dict["TN"] = "Total energy excluding the sector's share of electrical system energy losses."
e_type_dict["TP"] = "Resident population"
e_type_dict["UO"] = "Unfinished oils"
e_type_dict["US"] = "Unfractionated stream"
e_type_dict["WD"] = "Wood"
e_type_dict["WS"] = "Waste"
e_type_dict["WW"] = "Wood and waste"
e_type_dict["WX"] = "Waxes"
e_type_dict["WY"] = "Electricity produced from wind energy"
'''
s_type_dict["A"] = "the transportation sector"
s_type_dict["C"] = "the commercial sector"
s_type_dict["E"] = "the electric power sector"
s_type_dict["F"] = "E"
s_type_dict["G"] = "F"
s_type_dict["H"] = "the residential and commercial sectors"
s_type_dict["I"] = "the industrial sector"
s_type_dict["K"] = "consumed at coke plants"
s_type_dict["L"] = "(+C) from the production of fuel ethanol"
s_type_dict["M"] = "marketed production"
s_type_dict["N"] = "net imports"
s_type_dict["O"] = "(+C) the industrial sector other than"
s_type_dict["P"] = "(+R) production"
s_type_dict["R"] = "the residential sector"
s_type_dict["S"] = "S"
s_type_dict["T"] = "Total"
s_type_dict["V"] = "consumed as vehicle fuel"
s_type_dict["X"] = "all sectors excluding refinery fuel"

with open(data_file, 'r') as f:
	csv_reader = csv.DictReader(f)
	for row in csv_reader:
#		X.append([row['MSN'], row['StateCode'], int(row['Year']), float(row['Data'])])
		energy_type = row['MSN'][0:2]
		sector_type = row['MSN'][2:4]
		unit_type = row['MSN'][4]
		y = []
		y.append(energy_type)
		y.append(sector_type)
		'''
		if sector_type in ['A', 'C', 'F', 'G', 'H', 'I', 'K', 'M', 'N', 'R', 'S', 'T', 'V', 'X']:
			y.append(s_type_dict[sector_type])
		else:
			if sector_type == 'E':
				if consume_type == 'X':
					y.append('electricity export')
				else:
					y.append(s_type_dict[sector_type])
			elif sector_type == 'L':
				if consume_type == 'C':
					y.append(
		'''
		y.append(unit_type)
		tags.append(','.join(y))

with open('../tags.txt','w') as f:
	f.write('\n'.join(tags))
