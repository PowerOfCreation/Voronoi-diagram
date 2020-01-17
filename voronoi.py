import numpy as np
import random
import math
from matplotlib import pyplot as plt
from tqdm import tqdm

class Point():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def calculate_distance(self, second_point):  
        return calculate_distance(self, second_point.x, second_point.y)
    def calculate_distance(self, x, y):  
        dist = math.sqrt((x - self.x)**2 + (y - self.y)**2)  
        return dist 

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def get_random_points(width, height, amount):
    points = []
    for x in range(amount):
        points.append(Point(random.randint(0, width), random.randint(0, height), get_random_color()))
    
    return points

def get_closest_point(points, x, y):
    return points[np.argmin([point.calculate_distance(x, y) for point in points])]

width = 50
height = 50

points = get_random_points(width, height, 10)

image = np.zeros((height,width,3), np.uint8)

for y in tqdm(range(height), desc="Generating image"):
    for x in range(width):
        image[x, y] = get_closest_point(points, x, y).color

plt.imshow(image)

plt.savefig("image.jpg")

plt.show()