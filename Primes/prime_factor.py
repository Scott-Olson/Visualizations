import json, csv

prime_data = []
with open('primes_10k.csv', mode='r') as primes_in:
	primes = csv.reader(primes_in, delimiter = ',')
	print(primes)

# input will be a number
# output will be an array of the prime factors

# print(prime_data)

def is_prime(n):
	# checks if a number is prime or not
	if n == 2:
		return True

	for i in range(2, n // 2 + 1):
		if n % i == 0:
			return False
	return True

def prime_factor(num):
	# list of factors
	factors = []

	# should have to only check sqrt(num)
	for i in range(2, num // 2 + 1):
		if is_prime(i) and (num % i == 0):
			factors.append(i)

	return factors


# for the web visuliazation, need to seperate things into layers
# use json.dumps(data) to write to a json string
# def encode_factor_tree(factors):
# 	if

# test loop
for i in range(25, 35):
	print(i, is_prime(i))

print(prime_factor(34384))
# prime_factor(10)
# json_str = json.dumps(prime_factor(10))
# print(json_str)
