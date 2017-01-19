def find_missing(list1, list2):
	if isinstance(list1, list) == True:
            if isinstance(list2, list) == True:

            	ListDiff_1 = list(set(list1)-set(list2))
            	if ListDiff_1 == []:
            		ListDiff_2 = list(set(list2)-set(list1))