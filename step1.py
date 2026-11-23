# Ursina basics : windows, entities, game loop, input 

from ursina import * # Ursina engine: ntity, Camera, color, time, mouse...
import math #sin() for the back and forth movemnt 

# We create the application (window) and call it before creatign any Entity.
app = Ursina()

# THE GROUND
# An Entity is any object in the game (ground, cube, drone, gun,..)
# model : the 3D shape ('plane' = flat square, 'cube', 'sphere'...)
# scale : size (50 is 50 x 50 units plane)
# texture : image painted on the model ('white_cuube' = grid look)
# texture_scale : how many time ste texture repeats on eac axis 

floor = Entity(
    model = 'plane',
    scale = 50,
    color = color.dark_gray,
    texture = 'white_cube',
    texture_scale = (50,50),
)

# THE TARGET 
#Axes : x = right, y =  up,  z = foward (into screen).
# collider = 'box' gives the cube an invisble hitbox so the mous can detect it. Without a collider, clicks go straight through. 

aim = Entity(
    model ='cube',
    color = 'color.orange',
    position = (0,2,10), # 2 units high, 10 units in front of us 
    collser = 'box',
)

# CAMERA 
# We place the camera slightly above the ground, behid the origin, so we llok foward (+z) at the target. 
camera.position = (0,2,-5)

# Game loop
# Ursina calls update() automatically on EVERY frame (around 60 times/sec)
# This permits thing to me moving in the game.

def update():
    #time.dt : seconds elapsed since the previous frame. 
    # Multiplying a speed by time.dy makes movement frame-rate
    aim.rotation_y += 60 * time.dt

    #time.time() : current time in seconds, always increasing. 
    #sin() :  osscilates between -1 and 1, so x swings between -3 and 3.
    aim.x = math.sin(time.time()) * 3

# INPUT HANDLING
# Ursina calls input(key) once each time a key or mouse button is pressed. 'key' is a string like 'a', 'space', 'left mouse down'.

def inpt(key):
    #mouse.hovered_entity : the Entity under the cursor. Only works for Entities having a collider.
    if key == 'left mouse down' and mouse.hovered_entity == aim:
        aim.color = color.random_color() #Visual feedback on hit.

# START THE ENGINE : opens the window an runs the game loop until the window is closed. 
app.run()