from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# bg for the main background color 
bg = (0.0,0.0,0.0,0.0)
angle =0.0
rain_arrary = []

# draw_point function is extra just to see the pixels || show screen e akta function call hoiche||draw_points(250, 250)
def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()
# ++++++++++++++++++++++++++++++UNNECESSARY+++++++++++++++++++++++++++


#same as draw points first lab
def raindrop(a1,b1):  # create raindrop 
    glColor3f(0.0,0.0,1.0) #its pure blue
    glPointSize(3) #pixel size bydefault 1 thake
    glBegin(GL_POINTS) #must dite hobe as its a syntax 
    glVertex2f(a1, b1) #where i wanna plot the drops || points
    glEnd()

def rain_drops():
    # eita important 
    global angle
    for i in range(len(rain_arrary)):

        update_a, update_b,speed=rain_arrary[i]
        # Update the raindrop coordinate  angle e bakanor jonno 
        update_a +=  angle
        update_b -=  speed

        # Avoid raindow || jathe ghor e rain na dhuke
        if (update_b < 100) or (120 < update_a <380 and 100 < update_b < 300):
            update_a=random.uniform(100,400)
            update_b=random.uniform(300,500)
            speed=random.uniform(1,3)

        # Reset the raindrop if it goes off the screen
        # if update_b <0:
        #     update_a =random.uniform(100,400)
        #     update_b =random.uniform(300,500)
        #     speed =random.uniform(1,3)

        rain_arrary[i] = (update_a, update_b, speed)

# easy lab class theke bujsi 
def draw_house():
    glColor3f(1.0, 1.0, 0.0)  # Yellow color  house
    # glPointSize(5)
    glLineWidth(5)
    glBegin(GL_LINES)

    # Roof
    glVertex2f(400,300) # -
    glVertex2f(100,300)
    glVertex2f(400,300)#l
    glVertex2f(250,400)
    glVertex2f(100,300)#r
    glVertex2f(250,400)

    # Body
    glVertex2f(380, 300)
    glVertex2f(380, 100)
    glVertex2f(120, 300)
    glVertex2f(120, 100)
    glVertex2f(120, 100)
    glVertex2f(380, 100)
    glEnd()

    # glPointSize(5)
    # glLineWidth(2)
    # glBegin(GL_LINES)

    # glEnd()


def specialKeyListener(key, x, y):
    # first e angle set as 0.0
    global angle
    if key == GLUT_KEY_RIGHT:
        angle += 0.5
        print("Tilt Right")
    if key == GLUT_KEY_LEFT:
        angle -= 0.5
        print("Tilt Left")
    
    glutPostRedisplay()
    #  This function effectively notifies the GLUT system that the window's display should be refreshed as soon as possible.



def keyboardListener(key, x, y):
    global bg
    # n dile night hobe
    if key == b'n':
        bg = (0.0, 0.0, 0.0, 0.0) #black color 
    
        print("It's night")
        # m dile morning hobe
    if key == b'm':
        bg = (1.0, 1.0, 1.0, 1.0)
        print("It's morning")
    
    glutPostRedisplay()

# animation: Continuously updates raindrop positions and requests redisplay.
def animation():
    rain_drops()
    glutPostRedisplay()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClearColor(*bg)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    #extra to have some feel 
    draw_points(250, 250)
    draw_points(10, 10)
# ++++++++++++++++++++++++++++++++
    
    iterate()
    draw_house()
    
    # Call the raindrop function alltime cholbe
    for k in rain_arrary:
        raindrop(k[0], k[1])
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name

glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutIdleFunc(animation)
glutSpecialFunc(specialKeyListener)

# Random raindrop coordinates are stored in rain_arrary
# Populates the rain_arrary with initial random raindrop positions and speeds.
for j in range(550):
    x2 = random.uniform(100, 400)
    y2 = random.uniform(300, 500)
    speed = random.uniform(1, 3)
    rain_arrary.append((x2, y2, speed))

glutMainLoop()
