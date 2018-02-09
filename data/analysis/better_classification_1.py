import xlrd
import xlwt

# text_path = '../energy_type.txt'
# text_path2 = '../sector.txt'
# def proc_test(text_path):
# 	f = open(text_path, 'r')
# 	l = f.readlines()
# 	for i in range(len(l)):
# 		l[i] = l[i].lower().strip()
# 	return l

# tag_list = proc_test(text_path)
# print(tag_list)

# tag_list = proc_test(text_path2)
# print(tag_list)

data_path = '../ProblemCData.xlsx'
proc_energy_type_path = '../proc_energy_type.txt'
proc_sector_path = '../proc_sector.txt'
energy_type = ['aviation gasoline', 'asphalt and road oil', 'coal', 'biomass', 'crude oil', 'distillate fuel oil', 'electricity', 'fuel ethanol', 'fossil fuel', 'petrochemical feedstocks', '[gdp]', 'geothernal energy', 'heat pumps', 'hydroelectricity', 'jet fuel', 'kerosene', 'lpg', 'lubricants', 'motor gasoline', 'natural gasoline', 'natural gas', 'nuclear fuel', 'other petroleum products', 'all petroleum products', 'petroleum coke', 'primary energy', 'plant condensate', 'pentanes plus', 'renewable energy', 'residual fuel oil', 'supplemental gaseous fuels', 'still gas', 'special naphthas', 'photovoltaic and solar thermal energy', 'total energy', 'resident population', 'unfinished oils', 'unfractionated stream', 'wood', 'wood and waste', 'waxes']
sector = ['industrial', 'electric power', 'transportation', 'commercial', 'residential', 'total', 'end-use']
def proc_file(data_path, types):
	# global energy_type
	workbook = xlrd.open_workbook(data_path)
	sheet = workbook.sheet_by_index(1)
	n = sheet.nrows
	des_list = []
	for i in range(1,n):
		value = sheet.row_values(i)[1]
		new_string = value.lower().strip()
		# des_list_elem = []
		found = False
		for typ in types:
			if typ in new_string:
				found = True
				des_list.append(typ + '\n')
				break
		if(found == False):
			des_list.append('\n')
		# if new_string not in string_list:
			# string_list.append(new_string)
	return des_list

# proc_energy_type
des_list = proc_file(data_path, energy_type)
f = open(proc_energy_type_path,'w')
f.writelines(des_list)

print(des_list)

# proc_sector_path
des_list = proc_file(data_path, sector)
f = open(proc_sector_path,'w')
f.writelines(des_list)

print(des_list)
