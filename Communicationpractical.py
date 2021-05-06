 # -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:49:41 2021

@author: Andrew Hollington
The agents are interacting with the environment, 
sharing and storing with each other and eating the environment. The final 
position of these agents is then plotted. A number of iterations is definable
"""
#Import required modules

import random
import matplotlib.pyplot
import time
import agentframework_com
import csv

#Define functions used
#Obtain the distance between any two agents

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

#Read in the provided csv file to create the background environment 

f = open('csv.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in reader:
    rowlist = []				# A list of rows
    for value in row:
        rowlist.append(value)				# A list of value
        #print(value) 				# Floats
    environment.append(rowlist)

#time the process 

start = time.process_time()
    

#Define number of agents, iterations and the neighbourhood

num_of_agents = 10
num_of_iterations = 10
neighbourhood = 20

#create a list class called agents
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework_com.Agent(environment, agents))

# Move the agents
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)


 #Plot the axis
       
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

#Plot the environment

matplotlib.pyplot.imshow(environment)

#plot the agents 

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    
#Show the final plot

matplotlib.pyplot.show()

#Print the minimum and maximum distances if required

'''print(distance)
print(min(distance))
print(max(distance))'''

#Stop the timer and report the time 

end = time.process_time()

print("time = " + str(end - start))
f.close() 