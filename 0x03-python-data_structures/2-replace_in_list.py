#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
	low_val = 0
	high_val = len(my_list)
	if idx < low_val or idx > high_val:
		return None
	else:
		my_list[idx] = element
		return my_list
