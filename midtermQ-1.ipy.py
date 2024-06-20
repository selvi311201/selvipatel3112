#!/usr/bin/env python
# coding: utf-8

# # constructor that takes as input a pair of point objects that represent the end points of the line segment

# In[6]:


import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y
        return math.sqrt(dx**2 + dy**2)

    def slope(self):
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y
        if dx == 0:
            return None  # unbounded slope
        return dy / dx
p1 = Point(3, 4)
p2 = Point()
s = Segment(p1, p2)
print(s.length())  # 5.0
print(s.slope())  # 0.75


# In[ ]:




