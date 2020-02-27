# visualization of OEIS A220952
# http://oeis.org/A220952
# A twisted enumeration of the nonnegative integers.

# Definition:

# Say that nonnegative integers a and b are adjacent when their base-5 expansions ...a_2 a_1 a_0 and ...b_2 b_1 b_0 
# satisfy the condition that if i > j then the pairs of base-5 digits 
# (a_i,a_j) and (b_i,b_j) are either equal or consecutive in the path through {0, 1, 2, 3, 4}^2 shown at the diagram:
  # (0,4)--(1,4)--(2,4)--(3,4)  (4,4)
  #   |                    |      |
  #   |                    |      |
  # (0,3)  (1,3)--(2,3)  (3,3)  (4,3)
  #   |      |      |      |      |
  #   |      |      |      |      |
  # (0,2)  (1,2)  (2,2)  (3,2)  (4,2)
  #   |      |      |      |      |
  #   |      |      |      |      |
  # (0,1)  (1,1)  (2,1)--(3,1)  (4,1)
  #   |      |                    |
  #   |      |                    |
  # (0,0)  (1,0)--(2,0)--(3,0)--(4,0)


 
# first 15624 in csv adjacent
# CODE TO TRANSLATE THE ORIGINAL IMPORT CSV INTO CLEANER DATA
# a_csv = open('A220952_input.csv', mode="r").read().split('\n')
# b_csv = open('A220952_in.csv', mode="w")
# writer = csv.writer(b_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# for row in a_csv:
# 	temp = row
# 	temp2 = temp.split()
# 	writer.writerow([temp2[0], temp2[1]])

import matplotlib.pyplot as plt
# import numpy as np 
import pandas as pd

t = pd.read_csv('A220952_in.csv')


plt.plot(t['0'], t['0.1'], 'o')

plt.savefig("A220952.png")

