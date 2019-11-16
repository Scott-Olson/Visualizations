import numpy as np
import csv

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)//3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]


# generate all primes that are equal or less than a1.max() 
primes = primesfrom2to(10000000)


# print result    
print(primes, len(primes))


with open('primes_10m.csv', mode="w") as primes_file:
    prime_writer = csv.writer(primes_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(1, len(primes) + 1):
        prime_writer.writerow([i, primes[i - 1]])
