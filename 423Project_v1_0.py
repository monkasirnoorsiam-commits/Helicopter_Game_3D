from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 1000
window_width = 1200
text_indent_x = 10
text_indent_y = 30

map_y_size = 5000
map_x_size = 1000
cam_offset_y = 150
cam_offset_z = 700
rotor_angle = 0
helicopter_angle = -90
helicopter_tilt = 0
rotor_turn_speed = 4
player_z = 200
player_y = 0
player_x = 0
ghost_y = 0
min_player_y = -400
max_player_y = 300
min_player_x = -600
max_player_x = 600
camera_pos = [0, -map_y_size + cam_offset_y + player_y, cam_offset_z]
player_pos = [player_x, -map_y_size + 250 + player_y, player_z]
ghost_pos = [player_x, -map_y_size + 250 + ghost_y, player_z]
camera_lock = [0, -map_y_size + 250 + player_y, player_z]
backup_cam = camera_pos.copy()
initial_camera_offset = 150
fovY = 120
zNear = 0.1
zFar = 5000

GRID_LENGTH = 600
primary_fire = False
secondary_fire = False
player_speed = 10
cam_speed = 5
game = True
game_over = False
detail = 20
health = 100
score = 0
lives = 5
player_scene_speed = 0.15

def draw_text(x, y, text, font=GLUT_BITMAP_TIMES_ROMAN_24):
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, window_width, 0, window_height)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def draw_tree(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glPushMatrix()
    glColor3f(0.4, 0.25, 0.1)
    glTranslatef(0, 0, -45)
    gluCylinder(gluNewQuadric(), 15, 12, 50, 10, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.2, 0.6, 0.2)
    glTranslatef(0, 0, 50)
    gluSphere(gluNewQuadric(), 50, 10, 10)
    glPopMatrix()
    glPopMatrix()

def draw_house(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(90, 1, 0, 0)
    glScalef(1.25, 1.25, 1.25)
    glPushMatrix()
    glColor3f(0.8, 0.7, 0.5)
    glScalef(200, 150, 120)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.6, 0.3, 0.2)
    glTranslatef(0, 85, 0)
    glScalef(220, 40, 140)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.5, 0.25, 0.15)
    glTranslatef(0, 110, 0)
    glScalef(180, 30, 100)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.4, 0.25, 0.1)
    glTranslatef(0, -30, 61)
    glScalef(40, 70, 5)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.8, 0.7, 0.3)
    glTranslatef(15, -30, 64)
    gluSphere(gluNewQuadric(), 5, 10, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.7, 0.85, 0.95)
    glTranslatef(-60, 20, 61)
    glScalef(35, 35, 5)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.3, 0.2, 0.1)
    glTranslatef(-60, 20, 61)
    glScalef(40, 40, 3)
    glutWireCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.7, 0.85, 0.95)
    glTranslatef(60, 20, 61)
    glScalef(35, 35, 5)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.3, 0.2, 0.1)
    glTranslatef(60, 20, 61)
    glScalef(40, 40, 3)
    glutWireCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.7, 0.4, 0.3)
    glTranslatef(70, 120, 30)
    glScalef(25, 50, 25)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.6, 0.35, 0.25)
    glTranslatef(70, 150, 30)
    glScalef(30, 10, 30)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.6, 0.5, 0.4)
    glTranslatef(0, -80, 20)
    glScalef(80, 10, 60)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.9, 0.85, 0.75)
    glTranslatef(-35, -60, 50)
    glScalef(8, 50, 8)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.9, 0.85, 0.75)
    glTranslatef(35, -60, 50)
    glScalef(8, 50, 8)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.5, 0.3, 0.2)
    glTranslatef(0, -25, 60)
    glScalef(100, 10, 40)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.75, 0.7, 0.6)
    glTranslatef(150, -50, 0)
    glScalef(100, 100, 100)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.4, 0.35, 0.3)
    glTranslatef(150, -50, 51)
    glScalef(60, 70, 5)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.55, 0.3, 0.2)
    glTranslatef(150, 15, 0)
    glScalef(110, 15, 110)
    glutSolidCube(1)
    glPopMatrix()
    glPopMatrix()

def draw_helicopter():
    global player_pos, rotor_angle
    quadric = gluNewQuadric()
    glPushMatrix()
    glTranslatef(player_pos[0], player_pos[1], player_pos[2])
    glScalef(0.7, 0.7, 0.7)
    glRotatef(helicopter_angle, 0, 0, 1)
    glRotatef(helicopter_tilt, 1, 0, 0)
    glPushMatrix()
    glColor3f(0.15, 0.15, 0.18)
    glTranslatef(0, 0, 120)
    glScalef(2.2, 1.2, 1.0)
    gluSphere(quadric, 60, 10, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.1, 0.6, 0.9)
    glTranslatef(0, -45, 130)
    glScalef(1.5, 0.8, 0.7)
    gluSphere(quadric, 45, 10, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.05, 0.4, 0.7)
    glTranslatef(0, 40, 130)
    glScalef(1.5, 0.8, 0.7)
    gluSphere(quadric, 45, 10, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.15, 0.15, 0.18)
    glTranslatef(110, 0, 135)
    glRotatef(90, 0, 1, 0)
    gluCylinder(quadric, 25, 10, 190, 10, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.15, 0.15, 0.18)
    glTranslatef(300, 0, 135)
    glScalef(0.5, 0.5, 0.8)
    gluSphere(quadric, 25, 10, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.1, 0.1, 0.1)
    glTranslatef(0, 0, 180)
    gluCylinder(quadric, 8, 8, 30, 10, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.05, 0.05, 0.05)
    glTranslatef(0, 0, 215)
    glRotatef(rotor_angle, 0, 0, 1)
    glPushMatrix()
    glScalef(4.5, 0.12, 0.08)
    glutSolidCube(60)
    glPopMatrix()
    glPushMatrix()
    glRotatef(90, 0, 0, 1)
    glScalef(4.5, 0.12, 0.08)
    glutSolidCube(60)
    glPopMatrix()
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.25, 0.25, 0.25)
    glTranslatef(-25, -55, 60)
    glScalef(1.8, 0.12, 0.12)
    glutSolidCube(40)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.25, 0.25, 0.25)
    glTranslatef(-25, 55, 60)
    glScalef(1.8, 0.12, 0.12)
    glutSolidCube(40)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.25, 0.25, 0.25)
    glTranslatef(-30, -45, 85)
    glScalef(0.12, 0.12, 0.6)
    glutSolidCube(40)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.25, 0.25, 0.25)
    glTranslatef(30, -45, 85)
    glScalef(0.12, 0.12, 0.6)
    glutSolidCube(40)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.25, 0.25, 0.25)
    glTranslatef(-30, 45, 85)
    glScalef(0.12, 0.12, 0.6)
    glutSolidCube(40)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.25, 0.25, 0.25)
    glTranslatef(30, 45, 85)
    glScalef(0.12, 0.12, 0.6)
    glutSolidCube(40)
    glPopMatrix()
    glPopMatrix()

def keyboardListener(key, x, y):
    global player_pos, game, camera_pos, cam_speed, player_x, player_y, camera_lock, cam_offset_y, cam_offset_z, map_y_size, max_player_x, min_player_x, max_player_y, min_player_y
    if game:
        if key == b'w':
            if player_y < max_player_y:
                player_y += player_speed
                player_pos[1] += player_speed
            else:
                player_y = max_player_y
                player_pos[1] = max_player_y
        if key == b's':
            if player_y > min_player_y:
                player_y -= player_speed
                player_pos[1] -= player_speed
            else:
                player_y = min_player_y
                player_pos[1] = min_player_y
        if key == b'a':
            if player_x > min_player_x:
                player_x -= player_speed
                player_pos[0] -= player_speed
            else:
                player_x = min_player_x
                player_pos[0] = min_player_x
        if key == b'd':
            if player_x < max_player_x:
                player_x += player_speed
                player_pos[0] += player_speed
            else:
                player_x = max_player_x
                player_pos[0] = max_player_x
        camera_pos = [0, -map_y_size + cam_offset_y + ghost_y, cam_offset_z]
        camera_lock = [0, -map_y_size + 250 + ghost_y, player_z]
    if key == b'p':
        if game:
            game = False
        else:
            game = True
    if not game:
        if key == b',':
            camera_pos[2] -= cam_speed
        if key == b'.':
            camera_pos[2] += cam_speed
    glutPostRedisplay()
    # # Reset the game if R key is pressed
    # if key == b'r':

def specialKeyListener(key, x, y):
    global camera_pos, cam_speed
    x = camera_pos[0]
    y = camera_pos[1]
    if not game:
        if key == GLUT_KEY_UP:
            y += cam_speed
        if key == GLUT_KEY_DOWN:
            y -= cam_speed
        if key == GLUT_KEY_LEFT:
            x -= cam_speed
        if key == GLUT_KEY_RIGHT:
            x += cam_speed
    camera_pos[0] = x
    camera_pos[1] = y
    glutPostRedisplay()

def mouseListener(button, state, x, y):
    global primary_fire, secondary_fire
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        primary_fire = True
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        secondary_fire = True

def setupCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovY, window_width/window_height, zNear, zFar)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2],
              0, camera_lock[1], camera_lock[2],
              0, 0, 1)

def draw_player():
    global player_pos
    glPushMatrix()
    glTranslatef(player_pos[0], player_pos[1], 50)
    glScalef(3, 3, 3)

    glPushMatrix()
    glColor3f(48 / 255, 104 / 255, 68 / 255)
    glTranslatef(0, 0, 40)
    glutSolidCube(25)
    glTranslatef(0, 0, -5)
    glutSolidCube(25)
    glPopMatrix()

    glPushMatrix()
    glColor3f(223 / 255, 170 / 255, 139 / 255)
    glTranslatef(15, 13, 45)
    glRotatef(-90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 5, 2, 25, detail, detail)
    glPopMatrix()

    glPushMatrix()
    glColor3f(223 / 255, 170 / 255, 139 / 255)
    glTranslatef(-15, 13, 45)
    glRotatef(-90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 5, 2, 25, detail, detail)
    glPopMatrix()

    glPushMatrix()
    glColor3f(63 / 255, 0, 1)
    glTranslatef(10, 0, 5)
    gluCylinder(gluNewQuadric(), 5, 7, 18, detail, detail)
    glPopMatrix()

    glPushMatrix()
    glColor3f(63 / 255, 0, 1)
    glTranslatef(-10, 0, 5)
    gluCylinder(gluNewQuadric(), 5, 7, 18, detail, detail)
    glPopMatrix()

    glPushMatrix()
    glColor3f(192 / 255, 192 / 255, 192 / 255)
    glTranslatef(0, 13, 40)
    glRotatef(-90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 8, 3, 30, detail, detail)
    glPopMatrix()

    glPushMatrix()
    glColor3f(40 / 255, 40 / 255, 43 / 255)
    glTranslatef(0, 0, 67)
    gluSphere(gluNewQuadric(), 15, detail, detail)
    glPopMatrix()

    glPopMatrix()

def idle():
    global camera_pos, backup_cam, player_y, player_pos, camera_lock, cam_offset_y, cam_offset_z, map_y_size, ghost_y, max_player_y, min_player_y, rotor_angle
    if game:
        player_y += player_scene_speed
        ghost_y += player_scene_speed
        max_player_y += player_scene_speed
        min_player_y += player_scene_speed
        player_pos[1] = -map_y_size + 250 + player_y
        rotor_angle += rotor_turn_speed

        camera_pos = [0, -map_y_size + cam_offset_y + ghost_y, cam_offset_z]
        camera_lock = [0, -map_y_size + 250 + ghost_y, player_z]

    if not game:
        backup_cam = [0, -map_y_size + cam_offset_y + ghost_y, cam_offset_z]
    glutPostRedisplay()

def level_1():
    glPointSize(20)
    glBegin(GL_POINTS)
    glVertex3f(-GRID_LENGTH, GRID_LENGTH, 0)
    glEnd()

    glBegin(GL_QUADS)

    glColor3f(1, 1, 1)
    glVertex3f(map_x_size, -map_y_size, 0)
    glVertex3f(-map_x_size, -map_y_size, 0)
    glVertex3f(-map_x_size, 0, 0)
    glVertex3f(map_x_size, 0, 0)

    glEnd()
    draw_house(-500, -2500, 0)
    draw_tree(-300, -2900, 0)
    draw_tree(-200, -2100, 0)
    draw_house(400, -3500, 0)
    draw_tree(600, -4000, 0)
    draw_tree(200, -3200, 0)
    draw_helicopter()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, window_width, window_height)
    setupCamera()

    level_1()

    glColor3f(0, 0, 0)
    draw_text(text_indent_x-2, window_height-text_indent_y-2, f"Health: {health}")
    draw_text(text_indent_x-2, window_height-2*text_indent_y-2, f"Score: {score}")
    draw_text(text_indent_x-2, window_height-3*text_indent_y-2, f"Lives: {lives}")
    glColor3f(1, 1, 1)
    draw_text(text_indent_x, window_height-text_indent_y, f"Health: {health}")
    draw_text(text_indent_x, window_height-2*text_indent_y, f"Score: {score}")
    draw_text(text_indent_x, window_height-3*text_indent_y, f"Lives: {lives}")

    if not game:
        glColor3f(0, 0, 0)
        draw_text(window_width/2-2, window_height/2-2, f"Pause")
        glColor3f(1, 1, 1)
        draw_text(window_width/2, window_height/2, f"Pause")
    if game_over:
        glColor3f(0,0,0)
        text(window_width/2-2, window_height/2-2, f"Game Over!")
        glColor3f(1,1,1)
        text(window_width/2, window_height/2, f"Game Over!")
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_width, window_height)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow(b"Air Strike")

    glutDisplayFunc(showScreen)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)

    glutMainLoop()

if __name__ == "__main__":
    main()
