#import fitdecode
import numpy as np
import parse_fit
import matplotlib.pyplot as plt
#import matplotlib.widgets import Cursor, Button

file1 = 'example/single.fit'
file2 = 'example/zwift.fit'
#file1 = 'example/single2.fit'
#file2 = 'example/zwift2.fit'

p1 = parse_fit.getPower(file1)
p2 = parse_fit.getPower(file2)


newp1, newp2 = parse_fit.add_zero(p1, p2)
fig1 = plt.figure(0)
fig1 = plt.figure(figsize=(20,5))
plt.plot(newp1, label="single sided")
plt.plot(newp2, label="total output")


avg3p1 = parse_fit.moving_3sec_avg(newp1,time=10)
avg3p2 = parse_fit.moving_3sec_avg(newp2, time=10)
left_actual = avg3p1/2
LRPerc = []
for i in range(len(left_actual)):
    LRPerc.append(100*(left_actual[i]/avg3p2[i]))

avgLRPerc = parse_fit.moving_3sec_avg(np.array(LRPerc), time=10)

fig2 = plt.figure(1)
fig2, ax1 = plt.subplots()
fig2 = plt.figure(figsize=(20,5))
ax1.plot(avg3p1, label="3s avg single sided", linewidth=0.5)
ax1.plot(avg3p2, label="3s avg total output", linewidth=0.5)
ax1.legend()
ax2 = ax1.twinx()
ax2.set_ylim(0, 100)
ax2.plot(avgLRPerc, 'r', label="L/R difference")
ax2.plot([50 for i in range(len(LRPerc))], linewidth=0.5)
ax2.legend()
#plt.Cursor(horizOn = True, vertOn=True, color='green', linewidth=1.0)

plt.show()


