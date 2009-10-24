#This is the screne configuration file. It is used to set up the world for rendering.

#Relative to the screen -
#x axis- Left, Right
#y axis- Top, Botttom
#z axis: Outside, Inside

#Colors - R,G,B tuple where each component varies between zero and one.

from numpy import array

from light import Light
from sphere import Sphere
from plane import Plane
from vector3 import Vector3, UNIT_Y

#Description of the scene
#Eventually, this should be read from a file

#List of lights in this scene
lights = []

#List of objects in this scene
objects = []

#Background color
BGCOLOR = (0, 0, 0)

#Image size
IMAGE_SIZE = (1024, 768)

#Recursion Level
MAX_RECURSIONS = 3

def initialise_default_scene():
    #Initialise Lights
    position = Vector3(0, 50, -100)
    color = (1, 1, 1)

    light1 = Light(position, color)

    position2 = Vector3(0, 0, -100)
    color2 = (1, 1, 1)

    light2 = Light(position2, color2)
    #Initialise objects
    #Object 1
    center = Vector3(-30, 10, -130)
    radius = 10 
    color = (0, 0, 1)
    sphere1 = Sphere(center, radius, color)
    
    #Object2
    center2 = Vector3(0, 20, -100)
    radius2 = 10 
    color2 = (1, 0, 1)
    sphere2 = Sphere(center2, radius2, color2)

    #Object3: Ground plane
    normal = UNIT_Y
    distance = 2
    color3 = (0, 1, 1)
    plane1 = Plane(normal, distance, color3)

    globs = globals()
    #Add the objects to the object list
    globs['objects'].append(sphere2)
    globs['objects'].append(sphere1)
    globs['objects'].append(plane1)
    
    #Add lights to the light list
    globs['lights'].append(light1)
    globs['lights'].append(light2)
