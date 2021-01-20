from numpy import sin, cos

import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def multiplot(x1, y1, y1_2, x2, y2, y2_2, color1="blue", color2="orange",
              subtitle="", x1_label="", y1_label="", x2_label="", y2_label=""):

       fig, (ax1, ax2) = plt.subplots(2, 1)
       fig.suptitle(subtitle)

       ax1.plot(x1, y1, color=color1)
       try:
              ax1.plot(x1, y1_2, color=color2)
       except:
              pass
       ax1.set_xlabel(x1_label)
       ax1.set_ylabel(y1_label)
       ax1.legend((f"m1 {y1_label}", f"m2 {y1_label}"))

       ax2.plot(x2, y2,  color=color1)
       try:
              ax2.plot(x2, y2_2,  color=color2)
       except:
              pass
       ax2.set_xlabel(x2_label)
       ax2.set_ylabel(y2_label)
       ax2.legend((f"m1 {y2_label}", f"m2 {y2_label}"))

       plt.show()