from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

camera_pos = (500, 500, 400)
fovY = 60

helicopter_x = 0
helicopter_y = 0
helicopter_z = 0

helicopter_angle = 0

rotor_angle = 0

move_speed = 8
turn_speed = 4

helicopter_tilt = 0

keys = {
    b'w': False,
    b's': False,
    b'a': False,
    b'd': False
}

def draw_helicopter():

    global rotor_angle

    quadric = gluNewQuadric()

    glPushMatrix()

    glTranslatef(
        helicopter_x,
        helicopter_y,
        helicopter_z
    )

    glRotatef(
        helicopter_angle,
        0,
        0,
        1
    )


    glRotatef(
        helicopter_tilt,
        1,
        0,
        0
    )

    glPushMatrix()

    glColor3f(
        0.15,
        0.15,
        0.18
    )

    glTranslatef(
        0,
        0,
        120
    )

    glScalef(
        2.2,
        1.2,
        1.0
    )

    gluSphere(
        quadric,
        60,
        10,
        10
    )

    glPopMatrix()

    glPushMatrix()

    glColor3f(
        0.1,
        0.6,
        0.9
    )

    glTranslatef(
        0,
        -45,
        130
    )

    glScalef(
        1.5,
        0.8,
        0.7
    )

    gluSphere(
        quadric,
        45,
        10,
        10
    )

    glPopMatrix()

    glPushMatrix()

    glColor3f(
        0.05,
        0.4,
        0.7
    )

    glTranslatef(
        0,
        40,
        130
    )

    glScalef(
        1.5,
        0.8,
        0.7
    )

    gluSphere(
        quadric,
        45,
        10,
        10
    )

    glPopMatrix()

    glPushMatrix()

    glColor3f(
        0.15,
        0.15,
        0.18
    )

    glTranslatef(
        110,
        0,
        135
    )

    glRotatef(
        90,
        0,
        1,
        0
    )

    gluCylinder(
        quadric,
        25,
        10,
        190,
        10,
        10
    )

    glPopMatrix()

    glPushMatrix()

    glColor3f(
        0.15,
        0.15,
        0.18
    )

    glTranslatef(
        300,
        0,
        135
    )

    glScalef(
        0.5,
        0.5,
        0.8
    )

    gluSphere(
        quadric,
        25,
        10,
        10
    )

    glPopMatrix()

    glPushMatrix()

    glColor3f(
        0.1,
        0.1,
        0.1
    )

    glTranslatef(
        0,
        0,
        180
    )

    gluCylinder(
        quadric,
        8,
        8,
        30,
        10,
        10
    )

    glPopMatrix()

    glPushMatrix()

    glColor3f(
        0.05,
        0.05,
        0.05
    )

    glTranslatef(
        0,
        0,
        215
    )

    # Rotor rotation
    glRotatef(
        rotor_angle,
        0,
        0,
        1
    )

    glPushMatrix()

    glScalef(
        4.5,
        0.12,
        0.08
    )

    glutSolidCube(60)

    glPopMatrix()

    glPushMatrix()

    glRotatef(
        90,
        0,
        0,
        1
    )

    glScalef(
        4.5,
        0.12,
        0.08
    )

    glutSolidCube(60)

    glPopMatrix()

    glPopMatrix()

    glPushMatrix()

    glColor3f(
        0.25,
        0.25,
        0.25
    )

    glTranslatef(
        -25,
        -55,
        60
    )

    glScalef(
        1.8,
        0.12,
        0.12
    )

    glutSolidCube(40)

    glPopMatrix()

    glPushMatrix()

    glColor3f(
        0.25,
        0.25,
        0.25
    )

    glTranslatef(
        -25,
        55,
        60
    )

    glScalef(
        1.8,
        0.12,
        0.12
    )

    glutSolidCube(40)

    glPopMatrix()

    glPushMatrix()

    glColor3f(
        0.25,
        0.25,
        0.25
    )

    glTranslatef(
        -30,
        -45,
        85
    )

    glScalef(
        0.12,
        0.12,
        0.6
    )

    glutSolidCube(40)

    glPopMatrix()

    glPushMatrix()

    glColor3f(
        0.25,
        0.25,
        0.25
    )

    glTranslatef(
        30,
        -45,
        85
    )

    glScalef(
        0.12,
        0.12,
        0.6
    )

    glutSolidCube(40)

    glPopMatrix()

    glPushMatrix()

    glColor3f(
        0.25,
        0.25,
        0.25
    )

    glTranslatef(
        -30,
        45,
        85
    )

    glScalef(
        0.12,
        0.12,
        0.6
    )

    glutSolidCube(40)

    glPopMatrix()

    glPushMatrix()

    glColor3f(
        0.25,
        0.25,
        0.25
    )

    glTranslatef(
        30,
        45,
        85
    )

    glScalef(
        0.12,
        0.12,
        0.6
    )

    glutSolidCube(40)

    glPopMatrix()

    glPopMatrix()


def update_helicopter():

    global helicopter_x
    global helicopter_y
    global helicopter_angle
    global helicopter_tilt
    global rotor_angle

    moving = False

    if keys[b'a']:

        helicopter_angle += turn_speed

        helicopter_tilt = 10

        moving = True


    if keys[b'd']:

        helicopter_angle -= turn_speed

        helicopter_tilt = -10

        moving = True

    if keys[b'w']:

        angle = math.radians(
            helicopter_angle
        )

        helicopter_x -= (
            math.cos(angle) *
            move_speed
        )

        helicopter_y -= (
            math.sin(angle) *
            move_speed
        )

        moving = True

    if keys[b's']:

        angle = math.radians(
            helicopter_angle
        )

        helicopter_x += (
            math.cos(angle) *
            move_speed
        )

        helicopter_y += (
            math.sin(angle) *
            move_speed
        )

        moving = True


    if helicopter_x < -400:

        helicopter_x = -400

    if helicopter_x > 400:

        helicopter_x = 400

    if helicopter_y < -400:

        helicopter_y = -400

    if helicopter_y > 400:

        helicopter_y = 400

    if moving:

        rotor_angle += 35

        if rotor_angle >= 360:

            rotor_angle -= 360

    if not keys[b'a'] and not keys[b'd']:

        if helicopter_tilt > 0:

            helicopter_tilt -= 1

        elif helicopter_tilt < 0:

            helicopter_tilt += 1


def keyboardListener(key, x, y):

    if key in keys:

        keys[key] = True

def keyboardUpListener(key, x, y):

    if key in keys:

        keys[key] = False

def setupCamera():

    glMatrixMode(
        GL_PROJECTION
    )

    glLoadIdentity()

    gluPerspective(
        fovY,
        1.25,
        0.1,
        1500
    )

    glMatrixMode(
        GL_MODELVIEW
    )

    glLoadIdentity()

    x, y, z = camera_pos

    gluLookAt(
        x,
        y,
        z,
        0,
        0,
        120,
        0,
        0,
        1
    )

def showScreen():

    glClear(
        GL_COLOR_BUFFER_BIT |
        GL_DEPTH_BUFFER_BIT
    )

    glLoadIdentity()

    glViewport(
        0,
        0,
        1000,
        800
    )

    setupCamera()

    draw_helicopter()

    glutSwapBuffers()

def idle():

    update_helicopter()

    glutPostRedisplay()

def main():

    glutInit()

    glutInitDisplayMode(
        GLUT_DOUBLE |
        GLUT_RGB |
        GLUT_DEPTH
    )

    glutInitWindowSize(
        1000,
        800
    )

    glutInitWindowPosition(
        0,
        0
    )

    glutCreateWindow(
        b"3D Helicopter"
    )

    glEnable(
        GL_DEPTH_TEST
    )

    glutDisplayFunc(
        showScreen
    )

    glutKeyboardFunc(
        keyboardListener
    )

    glutKeyboardUpFunc(
        keyboardUpListener
    )

    glutIdleFunc(
        idle
    )

    glutMainLoop()

if __name__ == "__main__":

    main()