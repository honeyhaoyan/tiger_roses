import xlrd

workbook_path = '../ProblemCData_new.xlsx'
heads = {}
write_list = []
with xlrd.open_workbook(workbook_path) as f:
	sheet = f.sheet_by_index(1)
	n = sheet.nrows
	for i in range(1,n):
		row = sheet.row_values(i)
		heads[row[0]] = row[2]
	heads[''] = ''
	sheet = f.sheet_by_index(0)
	n = sheet.nrows
	for i in range(1,n):
		row = sheet.row_values(i)
		write_val = heads.get(row[0][0:2])
		write_list.append(write_val + '\n')

proc_path = '../cleanliness.txt'
with open(proc_path,'w') as f:
	f.writelines(write_list)
print(write_list)