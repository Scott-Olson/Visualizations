# Project Euler problem 719 - Number Splitting
# projecteuler.net/problem=719
# We define an S-number to be a natural number, n, 
# that is a perfect square and its square root can be obtained 
# by splitting the decimal representation of n into 2 or more numbers then adding the numbers.

# For example, 81 is an S-number because sqrt(81) = 8 + 1
# sqrt(6724) = 6 + 72 + 4
# T(N) is the sum of all S numbers in the range n <= N
# T(10**4) = 41333


# thought process:
# numbers that are a percect square are just the results of squaring integers
# so I can just calculate numbers that are below the square root of the target




import math

# permutation function that returns a set of possiblities
def permute(s):
	result = [[s]]
	for i in range(1, len(s)):
		first = [s[:i]]
		rest = s[i:]
		for p in permute(rest):
			result.append(first + p)
	return result


def snum(max):
	# possible S-numbers
	ps = []
	alt_in = int(math.sqrt(10**8)) + 1
	# int(math.sqrt(max)) + 1
	for i in range(alt_in, int(math.sqrt(max)) + 1):
		# holder element to make it easier to work on parts

		perm = permute(str(i**2))
		for p in perm:
			cur = perm[0][0]
			# sum of the values in the permutation, looking for solutions where this is equal to the sq root of the number(i)
			s = 0
			# length of the permutation string
			# solution for dealing with permutations where '01' and 1 are treated equally. 
			l = 0

			for k in p:
				l += len(str(k))
				s += int(k)
			# print('s: ', s, 'l: ', l, 'p: ', p, 'len: ', len(cur), 'cur: ', cur)
			if s == i and len(cur) >= 2 and l == len(cur) and i**2 not in ps:
				# print("cur: ", len(cur),' l: ', l)
				# print(p)
				ps.append(i**2)

	print(ps)
	return sum(ps)

print(snum(10**12))

# 10**4 = 41333
# test our method here, we know 10**4. lets try 10**4-10**8 and see if its the same
# 41333 + 2818811508 = 2818852841
# a difference of 10k, maybe a duplicate? increase the lower bound by 1 to get rid of included first element
# 41333 + 2818801508 = 2818842841
# so as long as the is the actual correct answer, the method should be correct
# 10**8 = 2818842841
# since we 'know' 10**8, we should only have to do 10**8+1 thru 10**12 and then sum them
# 2818842841 + 
# 10**12 = 






