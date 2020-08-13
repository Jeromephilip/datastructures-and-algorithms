# This is an introduction to Big O notation.

# O(1) Constant

def func_constant(values):
	print(values[0])

# O(n) Linear
# Drop constants if input gets large. For example, if there were 
# two of this loop, drop constant because if n was infinity, 2*infinity is infinity. 
def func_lin(lst):
	for val in lst:
		print(val)

# O(n^2) Quadratic
# Outputs n to the power 2 (ex. 10^2 --> 100 statements)
def func_quad(lst):
	for item_1 in lst:
		for item_2 in lst:
			print item_1, item_2

def comp(lst):
	print(lst[0]) #O(1)
	midpoint = len(lst)/2 # O(n/2 or 1/2n)
	for val in lst[:midpoint]:
		print(val)

	for x in range(10): # (O(10))
		print('HelloWorld')	
# Total O(1/2n + 1 + 10), but really as N gets larger, 
# these numbers become insignificant, so really it is O(n)

def check_match(lst, match):
	for val in list:
		if val == match:
			return true # If match = 1, then O(1), or if match = 5, then O(5)
	return false # Else it is O(n) where n is number of items in list. 

# In terms of Space Complexity

def printer(n):
	for x in range(n): # Here, the time complexity is O(n)
		print('Hello World') # But the Space Complexity, it is 1 as only 'Hello World' is being printed.


arr = [1,2,3,4,5,6]

