import xlrd

head_path = '../proc_energy_type.txt'

heads = []
with open(head_path, 'r') as f:
	heads = f.readlines()
	for i in range(len(heads)):
		heads[i] = heads[i].strip()

print(heads)
print('\n')

tags = {}
workbook_path = '../ProblemCData_new.xlsx'
with xlrd.open_workbook(workbook_path) as workbook:
	sheet = workbook.sheet_by_index(1)
	n = sheet.nrows
	for i in range(1,n):
		row = sheet.row_values(i)
		tags[row[0].lower()] = row[2:]
		# del row[1]
		# tags.append(row)
tags[''] = ['','','']
print(tags)	

output = []
for elem in heads:
	new_list = tags.get(elem)
	print(elem)
	print(new_list)
	new_string = '\t'.join(new_list) + '\n'
	output.append(new_string)

output_path = '../other_tags.txt'
with open(output_path, 'w') as f:
	f.writelines(output)
print(output)
