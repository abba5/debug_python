from datetime import datetime


def debug(obj, search_op = None):
	print(f'----------------- start {search_op} -------------')
	print()
	print()
	print(datetime.now())
	print(obj)
	print()
	print()
	print(f'-------------------end {search_op}--------------------')