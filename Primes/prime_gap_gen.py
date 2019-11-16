# import numpy as np 
import csv

# data to be imported and analyzed
with open('primes_10m.csv', mode="r") as primes_csv:
	primes = csv.reader(primes_csv, delimiter = ',')
	i = 1
	temp = 2
	with open('prime_gap.csv', mode="w") as pg_csv:
		pg_writer = csv.writer(pg_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		pg_writer.writerow(["order", "gap"])
		for row in primes:
			if int(row[1]) == 2:
				print("start")
				continue
			else:
				pg_writer.writerow([i, int(row[1]) - temp])
				temp = int(row[1])
				i += 1
			
		