import xlrd

data_path = '../ProblemCData.xlsx'
proc_path = '../processed.txt'

def proc_file(data_path):
	workbook = xlrd.open_workbook(data_path)
	sheet = workbook.sheet_by_index(1)
	n = sheet.nrows
	string_list = []
	for i in range(1,n):
		for j in range(1,5):
			value = sheet.row_values(i)[1]
			new_string = " ".join(value.split()[0:j]) + '\n'
			if new_string not in string_list:
				string_list.append(new_string)
	return string_list

with open(proc_path, "w") as f:
	ans = proc_file(data_path)
	print(ans)
	f.writelines(ans)