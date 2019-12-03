len1 = float(input('please input len1: '))
len2 = float(input('please input len2: '))
len3 = float(input('please input len3: '))

def cntPeremeter(l1, l2, l3):
	return l1 + l2 + l3

def cntArea(l1, l2, l3):
	p = (l1 + l2 + l3)/2
	return (p*(p-l1)*(p-l2)*(p-l3)) ** 0.5

if (len1 < len2 + len3) and \
(len2 < len1 + len3) and \
(len3 < len1 + len2):
	print('True\nperemeter:')
	print(cntPeremeter(len1, len2, len3))
	print('Area:\n')
	print(cntArea(len1, len2, len3))
else:
	print('False')

