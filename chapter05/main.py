#!Python3
'''
Chapter05 practice problems
Austin Cudoworth 9/19/19
'''

'''
-Display Inventory-
A function to display an item inventory
for a fantasy game.
'''

def displayInventory(inventory):

	itemqty = int() 
	print('\nInventory:')

	for k, v in inventory.items():
		
		itemqty += v	
		print(v,k)

	print('Total number of items:',itemqty,'\n')

myinv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(myinv)


'''
-Add to Inventory-
Function to take an inventory
defined as a dictionary object
and add an item to the inventory.
'''

def addToInventory(inventory, items):

	for item in items:

		if item in inventory.keys():

			inventory[item] = 1 + inventory.get(item)
		else:
			
			inventory[item] = 1

	return inventory


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(addToInventory(myinv,dragonLoot))
































