import control as co
from matplotlib import pyplot as plt

G = co.TransferFunction(1, (1, 125, 5100, 65000, 0))
rlist, klist = co.rlocus(G)
plt.show()
