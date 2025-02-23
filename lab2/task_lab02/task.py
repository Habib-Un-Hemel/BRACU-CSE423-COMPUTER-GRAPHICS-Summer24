import sys
import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *

window_width = 500
window_height = 500
diamond_size = 20
diamond_speed = 3.0
diamond_pos = [random.randint(0, window_width - diamond_size), window_height]
diamond_color = (random.random(), random.random(), random.random())
catcher_size = 50
catcher_pos = [window_width // 2 - catcher_size // 2, 10]
catcher_color = (1.0, 1.0, 1.0)  

score = 0
game_over = False
paused = False

button_size = 20
button_colors = {
    'restart': (0.0, 1.0, 1.0),   
    'play_pause': (1.0, 0.75, 0.0),  
    'exit': (1.0, 0.0, 0.0)     
}
button_states = {
    'play': True,
    'pause': False
}

def has_collided(box1, box2):
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2
    return (x1 < x2 + w2 and
            x1 + w1 > x2 and
            y1 < y2 + h2 and
            y1 + h1 > y2)

def restart_game():
    global score, diamond_speed, diamond_pos, diamond_color, game_over, catcher_color
    score = 0
    diamond_speed = 3.0
    diamond_pos = [random.randint(0, window_width - diamond_size), window_height]
    diamond_color = (random.random(), random.random(), random.random())  
    game_over = False
    catcher_color = (1.0, 1.0, 1.0)  
    print("Starting Over")
    glutPostRedisplay()

def play_pause():
    global paused
    paused = not paused
    button_states['play'] = not button_states['play']
    button_states['pause'] = not button_states['pause']
    glutPostRedisplay()

def exit_game():
    print(f"Goodbye! Your score: {score}")
    glutLeaveMainLoop()

def update(value):
    global diamond_pos, score, game_over, catcher_color, diamond_speed, diamond_color
    if not paused and not game_over:
        diamond_pos[1] -= diamond_speed
        diamond_speed += 0.01
        catcher_box = (catcher_pos[0] - catcher_size // 2, catcher_pos[1], catcher_size, catcher_size)
        diamond_box = (diamond_pos[0], diamond_pos[1], diamond_size, diamond_size)
        if has_collided(catcher_box, diamond_box):
            score += 1
            print(f"Score: {score}") 
            diamond_pos = [random.randint(0, window_width - diamond_size), window_height]
            diamond_color = (random.random(), random.random(), random.random())  
        if diamond_pos[1] < 0:
            game_over = True
            catcher_color = (1.0, 0.0, 0.0)  
            print(f"Game Over! Your final score: {score}")  

    glutTimerFunc(30, update, 0)
    glutPostRedisplay()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  

def findzone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx >= 0 and dy < 0:
            return 7
        elif dx < 0 and dy >= 0:
            return 3
        else:
            return 4
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx >= 0 and dy < 0:
            return 6
        elif dx < 0 and dy >= 0:
            return 2
        else:
            return 5

def convertToZone0(zone, x, y):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y

def originalZone(zone, x, y):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y

def draw_line(x1, y1, x2, y2):
    def draw_line_raw(zone, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        d = 2 * dy - dx
        dNE = 2 * (dy - dx)
        dE = 2 * dy

        x, y = x1, y1

        while x <= x2:
            cx, cy = originalZone(zone, x, y)
            glVertex2f(cx, cy)
            x += 1
            if d > 0:
                y += 1
                d = d + dNE
            else:
                d = d + dE

    zone = findzone(x1, y1, x2, y2)
    x1, y1 = convertToZone0(zone, x1, y1)
    x2, y2 = convertToZone0(zone, x2, y2)
    
    glBegin(GL_POINTS)
    draw_line_raw(zone, x1, y1, x2, y2)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    glColor3f(1.0, 1.0, 0.0)
    glPointSize(1)  
    glBegin(GL_POINTS)
    draw_line(100, 100, 200, 400)
    glEnd()

    glutSwapBuffers()

def draw_diamond(x, y, size, color):
    glColor3f(*color)
    draw_line(x, y, x + size // 2, y - size // 2)
    draw_line(x + size // 2, y - size // 2, x, y - size)
    draw_line(x, y - size, x - size // 2, y - size // 2)
    draw_line(x - size // 2, y - size // 2, x, y)

def draw_catcher(x, y, size, color):
    glColor3f(*color)
    draw_line(x - size // 2, y, x + size // 2, y)
    draw_line(x + size // 2, y, x + size // 4, y + size // 2)
    draw_line(x + size // 4, y + size // 2, x - size // 4, y + size // 2)
    draw_line(x - size // 4, y + size // 2, x - size // 2, y)

def draw_buttons():
    glColor3f(*button_colors['restart'])
    draw_line(20, window_height - 20, 40, window_height - 30)
    draw_line(40, window_height - 10, 20, window_height - 20)

    glColor3f(*button_colors['play_pause'])
    if button_states['play']:
        draw_line(window_width // 2 - 10, window_height - 20, window_width // 2 + 10, window_height - 25)
        draw_line(window_width // 2 + 10, window_height - 25, window_width // 2 + 10, window_height - 15)
        draw_line(window_width // 2 + 10, window_height - 15, window_width // 2 - 10, window_height - 20)
    else:
        draw_line(window_width // 2 - 10, window_height - 25, window_width // 2 + 10, window_height - 25)
        draw_line(window_width // 2 + 10, window_height - 25, window_width // 2 + 10, window_height - 15)
        draw_line(window_width // 2 + 10, window_height - 15, window_width // 2 - 10, window_height - 15)
        draw_line(window_width // 2 - 10, window_height - 15, window_width // 2 - 10, window_height - 25)

    glColor3f(*button_colors['exit'])
    draw_line(window_width - 40, window_height - 30, window_width - 20, window_height - 10)
    draw_line(window_width - 20, window_height - 30, window_width - 40, window_height - 10)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_diamond(diamond_pos[0], diamond_pos[1], diamond_size, diamond_color)
    draw_catcher(catcher_pos[0], catcher_pos[1], catcher_size, catcher_color)
    draw_buttons()
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def special_keys(key, x, y):
    global catcher_pos
    if not paused and not game_over:
        if key == GLUT_KEY_LEFT:
            catcher_pos[0] = max(catcher_pos[0] - 10, catcher_size // 2)
        elif key == GLUT_KEY_RIGHT:
            catcher_pos[0] = min(catcher_pos[0] + 10, window_width - catcher_size // 2)
    glutPostRedisplay()

def mouse(button, state, x, y):
    global paused, game_over
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 20 <= x <= 40 and window_height - 30 <= window_height - y <= window_height - 10:
            restart_game()
        elif window_width // 2 - 10 <= x <= window_width // 2 + 10 and window_height - 25 <= window_height - y <= window_height - 15:
            play_pause()
        elif window_width - 40 <= x <= window_width - 20 and window_height - 30 <= window_height - y <= window_height - 10:
            exit_game()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"Catch the Diamonds!")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(special_keys)
    glutMouseFunc(mouse)
    init()
    glutTimerFunc(30, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
