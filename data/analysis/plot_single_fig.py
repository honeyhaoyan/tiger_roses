from analysis import *

single_state_percentage_stacked_bar_chart_by_matrix(
	get_matrix('sector',['AC','CC','IC','RC'], stable_type=['Energy type','unit2'], s_type=['TE','V']),
	['Transportation','Commercial','Industrial','Residential'], title = "expenditure")

single_state_stacked_bar_chart_by_matrix(
	get_matrix('sector',['AC','CC','IC','RC'], stable_type=['Energy type','unit2'], s_type=['TE','V']),
	['Transportation','Commercial','Industrial','Residential'], title = "expenditure")

single_state_percentage_stacked_bar_chart_by_matrix(
	get_matrix('sector',['AC','CC','IC','RC'], stable_type=['Energy type','unit2'], s_type=['TE','B']),
	['Transportation','Commercial','Industrial','Residential'], title = "consumption")

single_state_stacked_bar_chart_by_matrix(
	get_matrix('sector',['AC','CC','IC','RC'], stable_type=['Energy type','unit2'], s_type=['TE','B']),
	['Transportation','Commercial','Industrial','Residential'], title = "consumption")
