# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x=np.linspace(-2*np.pi,2*np.pi,100)
y = np.sinc(x)

fig,ax = plt.subplots(ncols=2,figsize=(24,16))
ax[0].plot(x,y)
ax[0].set_title('pojedyncza krzywa')
ax[1].plot(x,y)
ax[1].plot(x*2.0,y)
ax[1].set_title('Dwie krzywe')
plt.show()

