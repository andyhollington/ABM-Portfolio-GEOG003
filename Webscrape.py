# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 19:15:58 2021

@author: Andrew Hollington

A set of agents is defined with initial positions on a grid defined through 
a webscrape to get initial positions.
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
import agentframework
import csv
import matplotlib.animation 
import bs4
import requests


#Define functions used

#Update model for each frame of the animation

def update(frame_number):    
    fig.clear()   
    global carry_on    
    carry_on = False
    random.shuffle(agents)
    for i in range(num_of_agents):
        #print(agents[i].store)
        agents[i].move()
        #print(agents[i].store)
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
    global carry_on 
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

    root.destroy() 

#Start main program

#Start the timer to time the process

start = time.process_time()

#Request initial starting positions for the agents from webpage

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text

#Use Beautiful Soup to extract values

soup = bs4.BeautifulSoup(content, 'html.parser')
td_y = soup.find_all(attrs={"class" : "y"})
td_x = soup.find_all(attrs={"class" : "x"})

#Strip the text to extract x and y values from the table

yy=[]
for ic in range(len(td_y)):
    yy.append(int(td_y[ic].get_text(strip=True)))
xx=[]
for ic in range(len(td_x)):
    xx.append(int(td_x[ic].get_text(strip=True)))



#Create initial pyplot figure

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



#Build the environment from csv raster data values given

f = open('csv.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in reader:
    rowlist = []				# A list of rows
    for value in row:
        rowlist.append(value)				# A list of value
        #print(value) 				# Floats
    environment.append(rowlist)
    
#Set parameters for the number of agents and the neighbourhood size


num_of_agents = 100
neighbourhood = 20

#Create the agents

agents = [] #initialise empty list

# Add if statement to ensure more than 100 agents can be used.
# Additional agents will be set to random through the append call from
#   the Agentframework

for i in range(num_of_agents):
    y=None
    x=None
    if i<len(yy):
        y = int(yy[i])
        x = int(xx[i])
    agents.append(agentframework.Agent(y, x, environment, agents))
    
# Create carry on, which defines the iteration's end and definitions to enable the agents to move, 
#  eat and interact with one another as well as to shuffle the order 
#  as to which agent is processed first following each movement
 
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
