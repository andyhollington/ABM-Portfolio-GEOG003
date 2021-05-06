# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:49:41 2021

@author: Andrew Hollington

A set of agents is defined with initial positions on a grid defined through 
a random generation
These agents are then set to move, eat and interact with one another consuming
the resources in the imported environment. The number of iterations is defined
by how much the agents have eaten.

"""

#Import required moodules

import random
import matplotlib.pyplot
import time
import agentframeworkOri
import csv
import matplotlib.animation 

#Define functions used
#Update model for each frame of the animation

def update(frame_number):
    
    fig.clear()   
    global carry_on

    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood) 
        
    

    if random.random() < 0.1:
            carry_on = False
            #print("stopping condition")
    
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.imshow(environment)

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.show()
    
# Keeps the agent moving if the agent has less than a certain amount (a) of 
# the environment and ends the process once it has reached that amount.
    
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
    

#set up the initial figure

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

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
    
#agent_1 = agentframework.Agent()
#agent_2 = agentframework.Agent()

#print(agent_1)

start = time.process_time()
    
#Define the number of agents and the neighbourhood size

num_of_agents = 100
neighbourhood = 20

agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframeworkOri.Agent(environment, agents))
    
carry_on = True	
    

animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()

#Stop the timer and print the time taken

end = time.process_time()
print("time = " + str(end - start))
f.close() 

