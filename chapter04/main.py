#! Python3
'''
Practice problems from chapter 04
by Austin Cudworth, 9/18/19
'''

'''
-Comma Code-
Concatenates a string of list input
with commas between each list item
and a comma-and between the second to last
and last item.
'''
def commacode(list):
	cdstring = ''

	for i in range(len(list)-1):
		cdstring += str(list[i]) + ', '

	cdstring += 'and ' + list[-1]

	return cdstring

mylist = ['apples','peaches','grapes','watermelon']

print(commacode(mylist))


'''
-Character Picture Grid-
Script that prints an input list of lists
in a transposed format, in this case
a heart shape is printed.
'''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print()

for j in range(len(grid[0])):

	for i in range(len(grid)):

		print(grid[i][j],end='')

	print()

print()




