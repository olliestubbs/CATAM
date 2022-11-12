import matplotlib.pyplot as plt
import numpy as np
xaxis = np.arange(0.4,2.5,0.01)
yaxis = xaxis*4-1

yaxis = np.log(yaxis)
yaxis = np.divide(yaxis,xaxis)
plt.plot(xaxis,yaxis)
plt.scatter([0.4,0.5,0.6,1,2],[-1.242,0.032,0.589,1.123,0.984],color = 'black')
plt.grid()
plt.xlabel('value of h')
plt.ylabel('estimated value of gamma')
plt.show()
