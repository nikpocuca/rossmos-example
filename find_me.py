import numpy as np 
import matplotlib.pyplot as plt 


# how to load images 
im = plt.imread("etobicoke.png")[:,:,:3]

# how to manipulate images! 
plt.imshow(im)
plt.show()

# Shopping at starsky!
im[600:630,500:540] = np.array([1.0,0.0,0.0])
plt.imshow(im) 
plt.show() 


# find me using the following addresses ! 

# greenfield park 
# 10 Wilmar Rd, Etobicoke, ON M9B 3R7, Canada

# yellow cup cafe 
# 225 The East Mall, Etobicoke, ON M9B 6J1

# kipling station 
# St Albans Rd, Toronto, ON

# old mill bakery 
# 385 The West Mall, Etobicoke, ON M9C 1E7

# planet bowl bowling alley  
# 5555 Eglinton Ave W, Etobicoke, ON M9C 5M1

# loblaws 
# 380 The East Mall, Etobicoke, ON M9B 6L5

# california sandwhiches 
# 1603 The Queensway, Etobicoke, ON M8Z 1T8


