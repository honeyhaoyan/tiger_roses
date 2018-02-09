from analysis import *

'''
plot_percentage_stacked_bar_chart(
	'cleanliness',
	['unclean energy', 'clean energy']
	)
'''
plot_tag_unit(
	'total energy', 'total', 'Million Btu')
plot_percentage_stacked_bar_chart(
	'sector',
	['commercial', 'transportation', 'residential', 'industrial'],
	['Energy type', 'Unit'],
	['wood', 'Billion Btu']
	
	)

plot_stacked_bar_chart(
	'sector',
	['commercial', 'transportation', 'residential', 'industrial'],
	['Energy type', 'Unit'],
	['wood', 'Billion Btu'],
	ylim='same'
	)

