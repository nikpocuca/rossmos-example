import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


richard_chase_sites = np.array([
    [3,17], 
    [15,3],
    [19,27], 
    [21,22], 
    [25,18]
]) 

richard_chase_residence = np.array([19,17])

def rossmos_formula(B: float, 
                    g: float, 
                    f: float, 
                    grid_x:float, 
                    grid_y:float, 
                    crime_x:float, 
                    crime_y:float):
    """
       B is the barrier 
       g is some constant 
       f is some constant  
    """

    d_xy = np.abs(grid_x - crime_x) + np.abs(grid_y - crime_y)
    indicator = float(d_xy > B)
    if d_xy > B:
        p_xy =  1.0 / (d_xy ** f)
    else: 
        p_xy = (B ** (g - f))  / ((2*B - d_xy) ** g)
    
    return p_xy

if __name__ == "__main__":

    # set up grid. 
    x = np.arange(1,31)
    y = np.arange(1,31)
    xx, xy = np.meshgrid(np.arange(1,31),np.arange(1,31))    
    plt.scatter(xx, xy, color ="black", s = 1)
    plt.scatter(richard_chase_sites[:,0], richard_chase_sites[:,1], color = "red", s = 50)
    plt.scatter(richard_chase_residence[0], richard_chase_residence[1], color = "blue", s = 50)
    # plt.show()

    # rossmos formula 
    PXY = np.zeros((30,30)) 

    for i in range(30):
        for j in range(30): 
            for crime in richard_chase_sites:
                PXY[i,j] += rossmos_formula(B = 5, g = 1, f = 0.5, 
                            grid_x=x[i], grid_y=y[j], 
                            crime_x = crime[0], crime_y = crime[1])

    
    plt.imshow(PXY, cmap='spring', interpolation='nearest')
    plt.title("Vampire of Sacremento")
    plt.savefig("vampire_of_sacremento.png")
    plt.show()
