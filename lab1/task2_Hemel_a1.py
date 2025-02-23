from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

listt = []  # List e point gula rakhbo || color 
# coordinates, color, speed, direction, and blink state).

speed =1.0  # akta surute speed initialize korsi
# flag =False  # control animation|| hudai laghe na 
back =True  #switching back color ||blinking
boundary_x = 500
boundary_y = 500
freeze = False  #freeze ar unfreeze kora hobe\\ Controls whether the points move or not.

# Time tracking for blinking
blink_time =time.time()
# print(time.time())

# time method eita
# Keeps track of time to toggle the blink state.

# same as task1
def draw_points(x,y,color):
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(color[0],color[1],color[2])
    glVertex2f(x,y)
    glEnd()


# 5point create shob random pore list dhukabo 
def create_random_point(x, y):
    # global er use raindrop e chilo
    global listt
    for i in range(5):
        color = create_random_color()
        runs = create_random_speed()
        direction_x, direction_y = cr_random_direction()
        listt.append({'x': x,'y': y,'color': color, 'black': [0, 0, 0], 'speed':runs, 'dx': direction_x, 'dy': direction_y, 'blink': False})

def create_random_color():
    return [random.random(), random.random(), random.random()]
#RGB thats why 3 random point 


def create_random_speed():
    return random.uniform(0.2, 0.3)*speed

def cr_random_direction():
    sign_x = random.choice([-1,1])
    sign_y = random.choice([-1,1])
    return sign_x, sign_y   
# It will randomly choose either -1 or 1.

def mouseClickListener(button, state, x, y):
    global listt, back
    # This parameter indicates the state of the mouse button. It can be either GLUT_DOWN (button pressed) or GLUT_UP (button released).
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        # x and y is storing the button clicking cordinates

        create_random_point(x, boundary_y - y)
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        toggle_blink()

# For each point, it flips the blink attribute's boolean value.
def toggle_blink():
    global listt
    for point in listt:
        point['blink'] = not point['blink']


# easy speed controler from here +++++++++++++++++++++++++++++++++
def specialKeyListener(key, x, y):
    global speed, flag, freeze
    if key == GLUT_KEY_UP:
        speed += 0.5
        update_speed()
    elif key == GLUT_KEY_DOWN and speed > 0.4:
        speed -= 0.5
        update_speed()

def update_speed():
    global listt
    for point in listt:
        point['speed'] = random.uniform(0.2, 0.3) * speed



def keyboard(key, x, y):
    # space ke eikhane
    if key == b' ': 
        button_freeze()


def button_freeze():
    global freeze
    freeze = not freeze

def animate():
    global listt, flag, boundary_x, boundary_y, freeze
    # if not freeze and not flag: hudai flag niye vab neyar try korislam but waste 
    if not freeze:
        for point in listt:
            point['x'] += point['dx'] * point['speed']
            point['y'] += point['dy'] * point['speed']
            # point['x'] += point['dx']
            # point['y'] += point['dy']
            # this thing just because speed barabe  na 

            # Bounce back  from  the  walls
            if point['x'] >=boundary_x or point['x'] <= 0:
                point['dx'] *= -1
            if point['y'] >=boundary_y or point['y'] <= 0:
                point['dy'] *= -1

    glutPostRedisplay()

def showScreen():
    global blink_time, back
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    iterate()

    current_time = time.time()

    # eita na thakle auto blink korbe na ,manually kora lagb blink
    if current_time - blink_time >= 0.5:
        back = not back
        blink_time = current_time

    global listt
    for point in listt:
        # blink jodi True and back jodi True then eikhane dhukbbo and black
        if point['blink'] and back:
            draw_points(point['x'], point['y'], point['black'])
        else:
            draw_points(point['x'], point['y'], point['color'])
    glutSwapBuffers()

#  task1 et same 
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
# same as task1
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
box = glutCreateWindow(b"Random Points")

glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseClickListener)
glutKeyboardFunc(keyboard)
glutMainLoop()
