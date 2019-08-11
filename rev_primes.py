# inspired by the Numberphile video Amazing Graphs with Neal Sloane
# https://www.youtube.com/watch?v=pAMgUB51XZA
# https://oeis.org/A265326
# nth prime minus its binary reversal

import matplotlib.pyplot as plt


fig = plt.figure()

# accepts int value, returns the prime value minus its binary reversal
def prime_rev(value):
	# formats the int into binary, filtering out the '0b' that is appended to python type?
	# bin(1) returns '0b1'
	# format(1, 'b') returns '1'
	temp = format(value, 'b')

	# slice trick to create a reversed list
	temp = temp[::-1]

	# return the initial value minus the int of reversed binary
	return value - int(temp, 2)

# function to check if a number is prime, could probably be optimized
def check_primes(value):
	for num in range(2, int(value/2)):
		if (value % num == 0):
			return False
	return True

		
# function to find prime numbers
def populate(prime_range):
	n = []
	an = []
	i = 2
	count = 1
	while i < prime_range:
		if(check_primes(i)):
			n.append(count)
			an.append(prime_rev(i))
			count += 1

		i += 1
	return n, an

data = populate(250000)

print(len(data[0]))

ax = fig.add_subplot(1,1,1)
ax.scatter(data[0], data[1], s = .5, color = 'black')
plt.show()




