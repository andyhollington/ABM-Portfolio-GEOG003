# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:48:47 2021

@author: Andrew Hollington
"""

#Import required modules

import random

class Agent():
    def __init__ (self, y, x, environment=[], agents=[]):
        self.environment = environment
        self.store = 0
        self.agents=agents
        if (x == None):
            self.x = random.randint(0,100)
        else:
            self.x = x
        if (y == None):
            self.y = random.randint(0,100)
        else:
            self.y = y
    
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    def share_with_neighbours(self, neighbourhood):
        #print(neighbourhood)
        for agent in self.agents:
            dist = self.distance_between(agent)
            #print(dist)
            if dist <= neighbourhood:
                ave = (self.store +agent.store)/2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))    
    def move(self):
        
        if random.random() <0.5:
            self.y =(self.y + 1) %100
        else:
            self.y =(self.y - 1) %100
            
        if random.random() <0.5:
            self.x =(self.x + 1) %100
        else:
            self.x =(self.x - 1) %100
            
            
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10