import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

from vampire_of_sacremento import rossmos_formula

de_salvo_sites = np.array([[10, 48], [13, 8], [15, 11], [17, 8], [18, 7],
  [18, 9], [19, 4], [19, 8], [20, 9], [20, 10], [20, 11],
  [29, 23], [33, 28]])

de_salvo_residence = np.array([19,18])


if __name__ == "__main__":

    # set up grid. 
    x = np.arange(1,31)
    y = np.arange(1,31)
    xx, xy = np.meshgrid(np.arange(1,31),np.arange(1,31))    
    plt.scatter(xx, xy, color ="black", s = 1)
    plt.scatter(de_salvo_sites[:,0], de_salvo_sites[:,1], color = "red", s = 50)
    plt.scatter(de_salvo_residence[0], de_salvo_residence[1], color = "blue", s = 50)
    # plt.show()

    # rossmos formula 
    PXY = np.zeros((30,30)) 

    for i in range(30):
        for j in range(30): 
            for crime in de_salvo_sites:
                PXY[i,j] += rossmos_formula(B = 10, g = 1, f = 0.5, 
                            grid_x=x[i], grid_y=y[j], 
                            crime_x = crime[0], crime_y = crime[1])

    
    plt.imshow(PXY, cmap='spring', interpolation='nearest')
    plt.title("Boston Strangler")
    plt.savefig("boston_strangler.png")
    plt.show()

