 
from OpenGL.GL import *
from OpenGL.GLUT import *
import random
 
dis=500
pause = False
score = 0
gameOver = False
shoot=False
cross_area=[0,0,0,0]
pause_area=[0,0,0,0]
resume_area=[0,0,0,0]
restart_area=[0,0,0,0]
five_circles_area=[]
Left = 0
Right = 0
s1,s2=5000,500
curr_x,curr_y=s1,s2
targetspeed=10
bulletspeed=500
bulletlist=[]
gameover= False
r,g,b=0,1,1
five_circle_list=[]
five_circle_area_list=[]
circle_x=[]
gone=False
clash=False
clash1=False
bothC=False
shooter_area=[0,0,0,0]
 
bcol=[]
def gen(x1):
  for x in range(5):
      y1=random.randint(6000,8000)
      rad=random.randint(100,500)
      five_circle_list.append([x1,y1,rad])
      five_circle_area_list.append([x1-rad,x1+rad,y1-rad,y1+rad])
      x1=x1+1500
  return
gen(2000)
 
def pauseGame():
  global pause
  if pause == False:
      pause = True
  else:
      pause = False
 
def draw_points(x0, y0):
  glPointSize(1)
  glBegin(GL_POINTS)
  glVertex2f(x0, y0)
  glEnd()
 
def midpoint(x0, y0, x1, y1):
  zone = findZone(x0, y0, x1, y1)
  x0, y0 = zoneConvert0(zone, x0, y0)
  x1, y1 = zoneConvert0(zone, x1, y1)
  dx = x1 - x0
  dy = y1 - y0
  dinit = 2 * dy - dx
  dne = 2 * dy - 2 * dx
  de = 2 * dy
  for i in range(x0, x1):
      a, b = convert_back_from_0(zone, x0, y0)
      if dinit >= 0:
          dinit = dinit + dne
          draw_points(a, b)
          x0 += 1
          y0 += 1
      else:
          dinit = dinit + de
          draw_points(a, b)
          x0 += 1
 
def findZone(x0, y0, x1, y1):
  dx = x1 - x0
  dy = y1 - y0
  if abs(dx) > abs(dy):
      if dx > 0 and dy > 0:
          return 0
      elif dx < 0 and dy > 0:
          return 3
      elif dx < 0 and dy < 0:
          return 4
      else:
          return 7
  else:
      if dx > 0 and dy > 0:
          return 1
      elif dx < 0 and dy > 0:
          return 2
      elif dx < 0 and dy < 0:
          return 5
      else:
          return 6
 
def zoneConvert0(zone, x0, y0):
  if zone == 0:
      return x0, y0
  elif zone == 1:
      return y0, x0
  elif zone == 2:
      return -y0, x0
  elif zone == 3:
      return -x0, y0
  elif zone == 4:
      return -x0, -y0
  elif zone == 5:
      return -y0, -x0
  elif zone == 6:
      return -y0, x0
  elif zone == 7:
      return x0, -y0
 
def convert_back_from_0(zone, x0, y0):
  if zone == 0:
      return x0, y0
  if zone == 1:
      return y0, x0
  if zone == 2:
      return y0, -x0
  if zone == 3:
      return -x0, y0
  if zone == 4:
      return -x0, -y0
  if zone == 5:
      return -y0, -x0
  if zone == 6:
      return y0, -x0
  if zone == 7:
      return x0, -y0
 
def specialKeyListener(key, left, right):
  glutPostRedisplay()
  global Left, Right, x0, x1,l1,r1,s1,s2,k1,k2,curr_y,curr_x
  if pause == False:
      if key == GLUT_KEY_LEFT:
          if s1 - Left + Right > 500:
              Left += 200
              curr_x=s1 - Left + Right
      elif key == GLUT_KEY_RIGHT:
          if s1 - Left + Right <= 9500:
              Right += 200
              curr_x=s1 - Left + Right
      glutPostRedisplay()
 
 
def keyboardListener(key, x, y):
  global shoot,l1,r1,s1,Left,Right,curr_y,curr_x,bulletlist,twi,clash1
  global bcol
  if key == b' ':
      shoot=True
      twi=True
      clash1=False
      bcol=[0,1,1]
      bulletlist.append([curr_x,curr_y,clash1,bcol])
  glutPostRedisplay()
 
 
def iterate():
  glViewport(0, 0, 500, 500)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glOrtho(0.0, 10000, 0.0, 10000, 0.0, 1.0)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
 
def mouseListener(button, state, x, y):
  global cross_area, pause_area, resume_area, restart_area,pause,five_circle_area_list
  global Left, Right,s1,s2,curr_x,curr_y,targetspeed,bulletspeed , bulletlist,score,circle_x,gone,gameOver
  global shoot,five_circle_list,five_circles_area,score,bothC,shooter_area,once,twi,countb,count
  if button == GLUT_LEFT_BUTTON:
      if (state == GLUT_DOWN):
          if restart_area[0]/20<=x<=restart_area[1]/20 and restart_area[2]/20<=500-y<=restart_area[3]/20:
              print(f"Game Restarted!! Previous Score: {score}")
              print('Restart')
              five_circles_area = []
              Left = 0
              Right = 0
              s1, s2 = 5000, 500
              curr_x, curr_y = s1, s2
              targetspeed = 20
              bulletspeed = 500
              bulletlist = []
              pause = False
              score = 0
              gameOver = False
              shoot = False
              five_circle_list = []
              five_circle_area_list = []
              circle_x = []
              gone = False
              bothC = False
              shooter_area = [0, 0, 0, 0]
              once = False
              twi = False
              countb = 0
              once = False
              twi = False
              countb = 0
              count=0
              gen(2000)
              glutPostRedisplay()
          if pause_area[0]/20<=x<=pause_area[1]/20 and pause_area[2]/20<=500-y<=pause_area[3]/20:
              pauseGame()
              glutPostRedisplay()
              print("Pause")
          if  resume_area[0]/20<=x<= resume_area[1]/20 and  resume_area[2]/20<=500-y<= resume_area[3]/20:
              print("Resume")
              glutPostRedisplay()
          if  cross_area[0]/20<=x<= cross_area[1]/20 and  cross_area[2]/20<=500-y<= cross_area[3]/20:
              print("GameOver")
              print('TotalScore:',score)
              glutLeaveMainLoop()
 
def restart_icon():
  global restart_area
  glColor3f(1.0, 0.0, 1.0)
  midpoint(200, 9400, 500, 9700)
  midpoint(200, 9400, 500, 9100)
  midpoint(200, 9400, 800, 9400)
  restart_area[0],restart_area[1],restart_area[2],restart_area[3]=200,800,9100,9700
 
 
def cross_icon():
  global cross_area
  glColor3f(0.0, 0.0, 1.0)
  midpoint(9200, 9700, 9800, 9100)
  midpoint(9200, 9100, 9800, 9700)
  cross_area[0],cross_area[1],cross_area[2],cross_area[3]=9200,9800,9100,9700
 
def pause_icon():
  global pause_area
  glColor3f(1.0, 1.0, 0.0)
  midpoint(4800, 9700, 4800, 9100)
  midpoint(5200, 9700, 5200, 9100)
  pause_area[0],pause_area[1],pause_area[2],pause_area[3]=4800,5200,9100,9700
 
def resume():
  global resume_area
  glColor3f(1.0, 1.0, 0.0)
  midpoint(4800, 9700, 4800, 9100)
  midpoint(4800, 9100, 5400, 9400)
  midpoint(4800, 9700, 5400, 9400)
  resume_area[0], resume_area[1], resume_area[2], resume_area[3] = 4800,5400,9100,9700
 
 
 
def draw_circle_shooter(x_centre, y_centre, radius):
  global shooter_area,Left,Right,shoot
  glColor3f(1.0, 0.0, 0.0)
  x, y = 0, radius
  d = 1 - radius
  glBegin(GL_POINTS)
  while x <= y:
      glVertex2f(x + x_centre-Left+Right, y + y_centre)
      glVertex2f(-x + x_centre-Left+Right, y + y_centre)
      glVertex2f(x + x_centre-Left+Right, -y + y_centre)
      glVertex2f(-x + x_centre-Left+Right, -y + y_centre)
      glVertex2f(y + x_centre-Left+Right, x + y_centre)
      glVertex2f(-y + x_centre-Left+Right, x + y_centre)
      glVertex2f(y + x_centre-Left+Right, -x + y_centre)
      glVertex2f(-y + x_centre-Left+Right, -x + y_centre)
      if d < 0:
          d += 2 * x + 3
      else:
          d += 2 * (x - y) + 5
          y -= 1
      x += 1
  glEnd()
 
 
def draw_circle_target(x_centre, y_centre, radius):
  global shooter_area,Left,Right,shoot
  glColor3f(1.0, 1.0, 0.0)
  x, y = 0, radius
  d = 1 - radius
  glBegin(GL_POINTS)
  while x <= y:
      glVertex2f(x + x_centre, y + y_centre)
      glVertex2f(-x + x_centre, y + y_centre)
      glVertex2f(x + x_centre, -y + y_centre)
      glVertex2f(-x + x_centre, -y + y_centre)
      glVertex2f(y + x_centre, x + y_centre)
      glVertex2f(-y + x_centre, x + y_centre)
      glVertex2f(y + x_centre, -x + y_centre)
      glVertex2f(-y + x_centre, -x + y_centre)
      if d < 0:
          d += 2 * x + 3
      else:
          d += 2 * (x - y) + 5
          y -= 1
      x += 1
  glEnd()
 
 
def draw_circle_bullet(x_centre, y_centre, radius,col):
  global shooter_area,Left,Right,shoot,clash1
  x, y = 0, radius
  d = 1 - radius
  r,g,b=col[0],col[1],col[2]
  glColor3f(r,g,b)
  glBegin(GL_POINTS)
  while x <= y:
      glVertex2f(x + x_centre, y + y_centre)
      glVertex2f(-x + x_centre, y + y_centre)
      glVertex2f(x + x_centre, -y + y_centre)
      glVertex2f(-x + x_centre, -y + y_centre)
      glVertex2f(y + x_centre, x + y_centre)
      glVertex2f(-y + x_centre, x + y_centre)
      glVertex2f(y + x_centre, -x + y_centre)
      glVertex2f(-y + x_centre, -x + y_centre)
      if d < 0:
          d += 2 * x + 3
      else:
          d += 2 * (x - y) + 5
          y -= 1
      x += 1
  glEnd()
 
 
def animate():
  global gone,pause,gameover
  if pause==False and gameover==False:
      if gone==False:
          animatetarget()
          animateshooter()
          glutPostRedisplay()
      else:
          pass
  else:
      pass
 
 
count=0
def animatetarget():
  global five_circle_list,targetspeed,shoot,s1,s2,k1,k2,bulletlist,bulletspeed,five_circle_area_list,five_circle_list,score,r
  global count,gone,s1,s2,Left,Right,score,bothC,shooter_area
  if count==3:
      gone=True
      print("GameOver")
      print("Total Score:",score)
  else:
      for cir in range(len(five_circle_list)):
          if five_circle_list[cir]==None:
              pass
          else:
              circle_y=five_circle_list[cir][1]
              circle_x=five_circle_list[cir][0]
              leftx,rightx=circle_x-five_circle_list[cir][2],circle_x+five_circle_list[cir][2]
              if bothC==True:
                  pass
              else:
                  k=circle_y-five_circle_list[cir][2]
                  if shooter_area[2]<=k<=shooter_area[3]:
                      if shooter_area[0]<=leftx<=shooter_area[1] or  shooter_area[0]<=rightx<=shooter_area[1]:
                          gone=True
                          print("Gameover")
                          print("Total Score:",score)
                  if circle_y<0 :
                      count+=1
                      five_circle_list[cir]=None
                  else:
                      circle_y=(circle_y-targetspeed)
                      five_circle_list[cir][1]=circle_y
once=False
twi=False
countb=0
def animateshooter():
  global five_circle_list,targetspeed,shoot,s1,s2,k1,k2,bulletlist,bulletspeed,five_circle_area_list,five_circle_list,score,r
  global once,dis,clash1,countb,gone
  if shoot==False:
      pass
  else:
      if countb//3 == 3:
          gone = True
          print("GameOver")
          print("Total Score:", score)
      else:
 
          for x in range(len(bulletlist)):
              if bulletlist[x]==None:
                  pass
              else:
                  b=bulletlist[x][1]
                  if 9000<=b<=10000 and bulletlist[x][3]==[0,1,1]:
                      countb+=1
                  a=bulletlist[x][0]
                  if clash1==True:
                      pass
                  else:
                      b=(b+bulletspeed)
                  for p in range(len(five_circle_area_list)):
                      if five_circle_area_list[p][0]<=a<=five_circle_area_list[p][1] and five_circle_area_list[p][2]<=b<=five_circle_area_list[p][3]:
                          temp=five_circle_list[p][0]
                          five_circle_list[p]=None
                          clash1=True
                          bulletlist[x][3]=[0,0,0]
                          if once==False:
                              k=random.randint(100,500)
                              five_circle_list[p]=[temp+dis,random.randint(6000,8000),k]
                              five_circle_area_list[p][0]=temp+dis-k
                              five_circle_area_list[p][1] = temp + dis + k
                              once=True
                          else:
                              k=random.randint(100,500)
                              five_circle_list[p]=[temp-dis,random.randint(6000,8000),k]
                              five_circle_area_list[p][0]=temp-dis-k
                              five_circle_area_list[p][1] = temp - dis + k
                              once=False
                          score += 1
                          if twi==True:
                              print("Score:", score)
                          else:
                              print("Score:", score-1)
                      else:
                          bulletlist[x][1] = b
 
def showScreen():
  global five_circle_list, s1, s2, shoot, bulletlist,shooter_area,Left,Right
  global bcol
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glLoadIdentity()
  iterate()
  glColor3f(0.0, 0.0, 0.0)
  restart_icon()
  cross_icon()
  if pause == False:
      pause_icon()
  else:
      resume()
  draw_circle_shooter(s1, s2, 300)
  shooter_area[0],shooter_area[1],shooter_area[2],shooter_area[3]=[s1-300-Left+Right,s1+300-Left+Right,s2-300,s2+300]
 
  for circle in five_circle_list:
      if circle is not None and len(circle) >= 3:
          draw_circle_target(circle[0], circle[1], circle[2])
  if shoot == True:
      if len(bulletlist) == 0:
          pass
      else:
          for bullet in bulletlist:
              if bullet is not None and len(bullet) >= 2:
                  draw_circle_bullet(bullet[0], bullet[1], 50,bullet[3])
              else:
                  pass
  glutSwapBuffers()
 
glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Game")
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboardListener)
glutMainLoop()
 