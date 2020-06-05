# -*- coding: utf-8 -*-
# @Author: chengdlin2
# @Date:   2020-03-26 17:10:57
# @Last Modified by:   chengdlin2
# @Last Modified time: 2020-03-26 17:11:00
# -*- coding: utf-8 -*-
# @Author: chengdlin2
# @Date:   2020-03-05 11:02:31
# @Last Modified by:   chengdlin2
# @Last Modified time: 2020-03-05 16:47:30
# headpose and eye track visualization

import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import h5py
import os.path as path


PATH = "D:/train/trainV2.hdf5"
index = 5000
for index in range(1):
    with h5py.File(PATH, 'r') as f:
        index = 500
        t = f['s02']['position_3d'][index]
        target = f['s02']['target'][index]
        x = np.linspace(-50,20,10)
        y = np.linspace(-30,100,10)

        X,Y = np.meshgrid(x,y)
        print(X.shape)
        Z=np.zeros(shape=(len(x), len(x)))

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlabel("x")
        ax.set_ylabel('z')
        ax.set_zlabel('y')
        ax.invert_yaxis()
        ax.invert_zaxis()
        ax.invert_xaxis()
        surf = ax.plot_surface(X, Z, Y, alpha=0.2, color='blue')
        ax.scatter(0,0,0)

        ax.plot3D(t[36:42,0], t[36:42,2], t[36:42,1], color='green', linewidth = 3)
        ax.plot3D(t[42:48,0], t[42:48,2], t[42:48,1], color='green', linewidth = 3)
        ax.plot3D(t[27:36,0], t[27:36,2], t[27:36,1], color='green', linewidth = 3)
        ax.plot3D(t[48:61,0], t[48:61,2], t[48:61,1], color='green', linewidth = 3)
        ax.scatter(t[-1,0], t[-1,2], t[-1,1], linewidths = 5, color='red')
        ax.scatter(t[-2,0], t[-2,2], t[-2,1], linewidths = 5, color = 'red')
        ax.plot3D([t[-1,0],target[0]], [t[-1,2], target[2]], [t[-1,1], target[1]])
        ax.plot3D([t[-2,0],target[0]], [t[-2,2], target[2]], [t[-2,1], target[1]])
        # ax.view_init(elev = 120, azim=90)
        plt.show()
        # def viz_head():
        #     return

        # def viz_target():
        #     return

        # def viz_gaze():
        #     return

def main():
    return