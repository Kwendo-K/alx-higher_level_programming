#!/usr/bin/python3
def element_at(my_list, idx):
	low_val = 0
	max_val = len(my_list)
	if idx < low_val or idx > max_val:
		return None
	else:
		return my_list[idx]
