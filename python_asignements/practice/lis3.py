def largest_of(lis1):
	max1 = lis1[0]
	for i in lis1:
		if i > max1:
			max1= i
	return max1
print largest_of([2,3,4,5,6])
