#!/usr/bin/python3
if __name__ == '__main__':
	import hidden_4
	for  i in dir(hidden_4):
		if not i.startwith("__"):
			print(":s".format(i))
