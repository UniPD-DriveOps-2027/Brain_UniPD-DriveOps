from cmath import sin
from zipapp import get_interpreter
import numpy as np
import matplotlib.pyplot as plt
PI = np.pi

R = 1.035  #-0.37/2     # big radius
r = 0.665  #-0.37/2    # small radius
L = 3.0    # horizontal distance

d = 0.001    # 0.0001 distance between points
m = 0.25   #+0.37/2  # border from the edge of the map
nl = 0.9     #no lane distance

NAME = 'no_lane_path_precise.npy'

assert r < R
assert (R + L + r) <= 6.0 - 2*m 
# assert (2*R + 0.4) <= 3.0 - 2*m

if __name__ == '__main__':

    # big arc
    #first half curve, below on the right
    th = np.linspace(0, -PI/2, round((0.5*PI*R/d)))
    g12_1 = np.array([1.5 + R*np.cos(th) , m+R + R*np.sin(th)])[:,:-1]
    print(f'g12 shape = {g12_1.shape}')

    #straight line below
    g12_2x = np.linspace(1.5, 1.5-nl, round((nl/d)))
    g12_2y = (m)*np.ones(round((nl)/d))
    g12_2 = np.vstack((g12_2x, g12_2y))[:,:-1]
    print(f'g45 shape = {g12_2.shape}') 

    #second half curve, below on left
    th = np.linspace(-PI/2, -PI, round((0.5*PI*R/d)))
    g12_3 = np.array([1.5-nl + R*np.cos(th) , m+R + R*np.sin(th)])[:,:-1]
    print(f'g12 shape = {g12_3.shape}')

    #left vertical straight line
    g23x = (1.5 - R - nl)*np.ones(round(L/d))
    g23y = np.linspace(m+R, m+R+L, round(L/d))
    g23 = np.vstack((g23x, g23y))[:,:-1]
    print(f'g23 shape = {g23.shape}') 

    #upper left curve
    th = np.linspace(-PI, -1.5*PI, round((0.5*PI*r/d)))
    g34x = (1.5-R+r-nl) + r*np.cos(th)
    g34y = (R+m+L) + r*np.sin(th)
    g34 = np.vstack((g34x, g34y))[:,:-1]
    print(f'g34 shape = {g34.shape}') 

    #upper straight
    g45x = np.linspace(1.5-R+r-nl, 1.5+R-r, round((2*(R-r)+nl)/d))
    g45y = (R+L+m+r)*np.ones(round((2*(R-r)+nl)/d))
    g45 = np.vstack((g45x, g45y))[:,:-1]
    print(f'g45 shape = {g45.shape}') 

    #upper right curve
    th = np.linspace(-1.5*PI, -2*PI, round((0.5*PI*r/d)))
    g56x = (1.5+R-r) + r*np.cos(th)
    g56y = (R+m+L) + r*np.sin(th)
    g56 = np.vstack((g56x, g56y))[:,:-1]
    print(f'g56 shape = {g56.shape}') 

    #right side straight line
    g61x = (1.5 + R)*np.ones(round(L/d))
    g61y = np.linspace(m+R+L, m+R, round(L/d))
    g61 = np.vstack((g61x, g61y))[:,:-1]
    print(f'g61 shape = {g61.shape}') 

    g = np.hstack((g12_1, g12_2, g12_3,g23,g34,g45,g56,g61)).T
    print(f'g shape = {g.shape}') 

    # g = g - np.array([0.0,0.37*0.5])

    diff = np.linalg.norm(g[1:]-g[:-1], axis=1)
    print(f'diff = {diff}')

    #plots
    g = g.T
    plt.plot(g[0],g[1])
    # g_ext = np.load('sparcs_path_ext_precise.npy')
    # g_int = np.load('sparcs_path_int_precise.npy')
    # plt.plot(g_ext[0],g_ext[1])
    # plt.plot(g_int[0],g_int[1])
    
    # plt.plot(diff)
    plt.axis('equal')

    # plt.ylim([-0.01,0.02])
    plt.show()

    #save the path
    np.save(NAME,g)
    print('path saved... exiting.')


