# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:20:37 2021

@author: Andrew Hollington
"""

#Import required modules

import random

#Create the sheep

class Agent():
    def __init__ (self, environment=[], agents=[]):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        self.environment = environment
        self.store = 0
        self.agents=agents
    
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
            
