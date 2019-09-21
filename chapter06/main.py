#!Python3

'''
Practice problems from ATBSWP
Chapter 06
'''

'''
-Table Printer-
Take a list of strings and print
a neat table with right-justified
columns.
'''

def printTable(table):

	colwidths = [0] * len(table) #list of column widths

	i = 0 #column counter

	for col in table:

		for row in col:
			
			if len(row) > colwidths[i]:

				colwidths[i] = len(row)

		i += 1 #increment counter

	print('\n',end='')

	for i in range(len(table[0])):

		for j in range(len(table)):

			print(table[j][i].rjust(colwidths[j]),end=' ')
		
		print('\n',end='')

	print('\n',end='')			


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)








































