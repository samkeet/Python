import sys 
def reverse(num):
	neg = False
	if num < 0:
		neg = True
		num = num*-1

	new_num = 0
	while num != 0:
		n = num%10
		new_num = new_num*10 + n
		num = num/10
	if neg:
		new_num = new_num*-1
	print new_num
	if new_num > sys.maxint:
		return 0
	else:
		return new_num

if __name__ == '__main__':
	print reverse(1534236469)

