# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:49:41 2021

@author: Andrew Hollington

A set of agents is defined with initial positions on a grid defined through 
a random function to give their initial positions.
These agents are then set to move, eat and interact with one another consuming
the resources in the imported environment. A simple menu is defined to start 
and quit the model.
"""


#Import required modules

import matplotlib
matplotlib.use('TkAgg')
import tkinter
import random
import matplotlib.pyplot
import time
import agentframeworkbeforewebscrape
import csv
import matplotlib.animation 

#Define functions used

#Update model for each frame of the animation
    
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    carry_on = False
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood) 
        carry_on =  bool (carry_on or  agents[i].store<100)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    
#plot environment and set of agents onto the environment
    
    matplotlib.pyplot.imshow(environment)

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

   
# Keeps the agent moving if the agent has less than a certain amount (a) of 
# the environment and ends the process once it has reached that amount.
    
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 50) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
#Runs the process as an animation

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    
#Stops the process running
    
def quit():

    root.quit()     # stops mainloop

    root.destroy()  # this is necessary on Windows to prevent

                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
                    
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



#Start main program

#Start the timer to time the process

start = time.process_time()
    

num_of_agents = 10
neighbourhood = 20

agents = []

# Make the agents

for i in range(num_of_agents):
    agents.append(agentframeworkbeforewebscrape.Agent(environment, agents))
    #print(agents[i].store)
    
carry_on = True

#Run the process 
#Putting in the menu with options 
                    
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 
model_menu.add_command(label="Quit model", command=quit) 

tkinter.mainloop()

#Stop the timer and report the time 

end = time.process_time()
print("time = " + str(end - start))
f.close() 
