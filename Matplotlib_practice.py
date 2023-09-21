import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

print(plt.style.available)
plt.style.use('dark_background')

Ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(Ages_x, py_dev_y, color='r', label='Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(Ages_x, js_dev_y, color='b', linewidth='3', label='JavaScript')

plt.plot(Ages_x, dev_y, color='y', linestyle='--', marker='o', label="Devs")

plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()

plt.tight_layout() # for good fit layout
plt.savefig("practice.png")
plt.show()
