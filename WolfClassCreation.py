# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:25:00 2021

@author: 44743
"""
import random

#Create the wolves
class Wolf():
    def __init__ (self, wolves=[], agent=[]):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        self.agent = agent
        #self.wolves = wolves
    
       
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
        for sheep in self.agent:
            dist = (((self.x - sheep.x)**2) + ((self.y - sheep.y)**2))**0.5
            #print (dist)
            if dist <5:
                
                #find which one in list
               # kill sheep
              # print (sheep)
               #self.num_of_agents -=1
               self.agent.remove(sheep)