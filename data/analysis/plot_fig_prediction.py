from analysis import *
from grey_prediction import *
import numpy as np


# plot_stacked_bar_chart_by_matrix(
# 	prediction(get_matrix('Energy type', ['EM','GE','HY','SO','WY','BM'], stable_type=['sector','unit2'], s_type=['TC','B'])),
# 	['Fuel ethanol excluding denaturant', 'geothermal energy', 'hydroelectricity', 'photovoltaic and solar thermal energy', 'wind electricity', 'biomass'], title="consumption_prediction",
# 	_ind=np.arange(2010,2060,1))

# plot_percentage_stacked_bar_chart_by_matrix(
# 	prediction(get_matrix('Energy type', ['EM','GE','HY','SO','WY','BM'], stable_type=['sector','unit2'], s_type=['TC','B'])),
# 	['Fuel ethanol excluding denaturant', 'geothermal energy', 'hydroelectricity', 'photovoltaic and solar thermal energy', 'wind electricity', 'biomass'], title="consumption_prediction",
# 	_ind=np.arange(2010,2060,1))

plot_stacked_bar_chart_by_matrix(
	prediction(get_matrix('Energy type', ['CL','NN','PM'], stable_type=['sector','unit2'], s_type=['TC','B'])),
	["Coal", "Natural gas", "Petroleum products"], title="consumption_prediction", _ind=np.arange(2010,2060,1))


plot_percentage_stacked_bar_chart_by_matrix(
	prediction(get_matrix('Energy type', ['CL','NN','PM'], stable_type=['sector','unit2'], s_type=['TC','B'])),
	["Coal", "Natural gas", "Petroleum products"], title="consumption_prediction", _ind=np.arange(2010,2060,1))

plot_percentage_stacked_bar_chart_by_matrix(
	prediction(get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['TC','B']) +
	get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['ET','B'])),
	["Fossil fuel", "nuclear power", "renewable energy"], title="consumption_prediction", _ind=np.arange(2010,2060,1))

plot_stacked_bar_chart_by_matrix(
	prediction(get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['TC','B']) +
	get_matrix('Energy type', ['FF','NU','RE'], stable_type=['sector','unit2'], s_type=['ET','B'])),
	["Fossil fuel", "nuclear power", "renewable energy"], title="consumption_prediction", _ind=np.arange(2010,2060,1))

plot_stacked_bar_chart_by_matrix(
	prediction(get_matrix('sector',['AC','CC','IC','RC'], stable_type=['Energy type','unit2'], s_type=['TE','B'])),
	['Transportation','Commercial','Industrial','Residential'], title = "consumption_prediction", _ind=np.arange(2010,2060,1))

plot_percentage_stacked_bar_chart_by_matrix(
	prediction(get_matrix('sector',['AC','CC','IC','RC'], stable_type=['Energy type','unit2'], s_type=['TE','B'])),
	['Transportation','Commercial','Industrial','Residential'], title = "consumption_prediction", _ind=np.arange(2010,2060,1))

