# inspired by the Numberphile video Amazing Graphs with Neal Sloane
# https://www.youtube.com/watch?v=pAMgUB51XZA
# https://oeis.org/A133058
# this is the sequence that I will try to plot and visualize, the Fly Straight, Dammit! 

import matplotlib.pyplot as plt
import numpy as np 

fig = plt.figure()

n = [0, 1]
fn = [1, 1]
loop_length = 1800
i = 2

while(i < loop_length):
	gcd = np.gcd(i, fn[i - 1])
	if gcd > 1:
		fn.append(int(fn[i - 1]/ gcd))
	elif gcd == 1:
		fn.append(fn[i - 1] + i + 1)
	n.append(i)
	i += 1

ax = fig.add_subplot(1,1,1)
ax.scatter(n, fn, s = 1, color = 'blue')
plt.show()







