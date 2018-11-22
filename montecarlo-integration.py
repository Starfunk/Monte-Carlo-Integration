# Monte Carlo method for integration!
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def func(x): # Given x, returns e^x^2
	return np.exp(x**2) 
	
def below(a1,a2): #a1 is the point on the curve, a2 is the rand point
	return (a1 > a2)
		
def montecarlo_integration():
	N = 10000000 # number of iterations - increase this for more accuracy
	x1 = 0 # left integration bound
	x2 = 2 # right integration bound
	y1 = 0 # framing the curve in a rectangle - lower bound
	y2 = func(x2) # framing the curve in a rectangle - upper bound
	tot_points = N
	points_below = 0
	for i in range(N): 
		point = random.uniform(x1,x2) #random x-coordinate
		y = random.uniform(y1,y2) #random y-coordinate
		if below(func(point),y): points_below += 1
	#dimensions of the rectangle
	width = x2 - x1
	height = y2 - y1
	return ((points_below/tot_points) * width * height)

print(montecarlo_integration())
