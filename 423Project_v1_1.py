from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

window_height = 800
window_width = 1000
text_indent_x = 10
text_indent_y = 30
map_y_size = [-20000, -5000, -5000]
map_x_size = [-2000, -2000, -2000]
house_positions = [
    [-500, -2500, 0], [400, -3500, 0], [-200, -4500, 0], [600, -1500, 0], [-400, -500, 0], [300, -4000, 0], [-100, -2000, 0], [500, -3000, 0],
    [-800, -6000, 0], [1000, -7000, 0], [-1200, -8000, 0], [1400, -9000, 0], [-600, -10000, 0], [800, -11000, 0], [-1000, -12000, 0], [1200, -13000, 0],
    [-400, -14000, 0], [600, -15000, 0], [-800, -16000, 0], [1000, -17000, 0], [-1200, -18000, 0], [1400, -19000, 0], [-200, -2000, 0], [200, -20000, 0]
]
garage_positions = [
    [-300, -2500, 0], [650, -3500, 0], [-100, -4500, 0], [700, -1500, 0], [-500, -500, 0], [450, -4000, 0], [-150, -2000, 0], [600, -3000, 0],
    [-700, -6500, 0], [1100, -7500, 0], [-1300, -8500, 0], [1500, -9500, 0], [-500, -10500, 0], [900, -11500, 0], [-1100, -12500, 0], [1300, -13500, 0],
    [-300, -14500, 0], [700, -15500, 0], [-900, -16500, 0], [1100, -17500, 0], [-1300, -18500, 0], [1500, -19500, 0], [-100, -2500, 0], [300, -15000, 0]
]
tree_positions = [
    [-300, -2900, 0], [-200, -2100, 0], [600, -4000, 0], [200, -3200, 0], [-400, -4800, 0], [500, -1800, 0], [-600, -400, 0], [400, -4200, 0],
    [-100, -2300, 0], [700, -3300, 0], [-450, -2800, 0], [250, -3800, 0], [-350, -1500, 0], [550, -2700, 0], [-50, -4700, 0], [650, -1700, 0],
    [-900, -5500, 0], [850, -6200, 0], [-700, -6800, 0], [750, -7500, 0], [-1100, -8200, 0], [1050, -8800, 0], [-650, -9500, 0], [950, -10200, 0],
    [-1250, -10900, 0], [1150, -11600, 0], [-550, -12300, 0], [850, -13000, 0], [-1150, -13700, 0], [1350, -14400, 0], [-450, -15100, 0], [750, -15800, 0],
    [-1050, -16500, 0], [1250, -17200, 0], [-350, -17900, 0], [650, -18600, 0], [-950, -19300, 0], [1450, -19800, 0], [-150, -20500, 0], [550, -21200, 0],
    [-1350, -2200, 0], [1300, -2800, 0], [-250, -3400, 0], [200, -4000, 0], [-1100, -4600, 0], [1000, -5200, 0], [-150, -5800, 0], [150, -6400, 0],
    [-1400, -7000, 0], [1400, -7600, 0], [-200, -8200, 0], [100, -8800, 0], [-1300, -9400, 0], [1200, -10000, 0], [-100, -10600, 0], [50, -11200, 0],
    [-1450, -11800, 0], [1450, -12400, 0], [-50, -13000, 0], [0, -13600, 0], [-1200, -14200, 0], [1100, -14800, 0], [-30, -15400, 0], [70, -16000, 0],
    [-1400, -16600, 0], [1350, -17200, 0], [-40, -17800, 0], [60, -18400, 0], [-1150, -19000, 0], [1300, -19600, 0], [-20, -20200, 0], [80, -20800, 0]
]
columns = [20, 20, 20]
rows = [100, 25, 25]
tile_size = 200
tiles = []

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
camera_pos = [0, map_y_size[0] + cam_offset_y + player_y, cam_offset_z]
player_pos = [player_x, map_y_size[0] + player_y, player_z]
ghost_pos = [player_x, map_y_size[0] + ghost_y, player_z]
camera_lock = [0, map_y_size[0] + 250 + player_y, player_z]
backup_cam = camera_pos.copy()
initial_camera_offset = 150
fovY = 120
zNear = 0.1
zFar = 2500

levels = 3
current_level = 1
secondary_fire = False
player_speed = 10
cam_speed = 5
game = True
game_over = False
detail = 20
health = 100
score = 0
lives = 5
player_scene_speed = 0.4

enemies = []
enemy_speed = 2
enemy_spawn_x = [-500, -250, 0, 250, 500]
enemy_spawn_index = 0

debug_mode = False
stealth_mode = False
power_level = 1  # 1: Single, 2: Dual, 3: Triple Spread
bullets = []     # Format: [x, y, z, vx, vy]
bullet_speed = 30

def keyboardListener(key, x, y):
    global debug_mode, player_pos, game, camera_pos, cam_speed, player_x, player_y, camera_lock, cam_offset_y, cam_offset_z, map_y_size, max_player_x, min_player_x, max_player_y, min_player_y, stealth_mode, power_level, enemies
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
        camera_pos = [0, map_y_size[0] + cam_offset_y + ghost_y, cam_offset_z]
        camera_lock = [0, map_y_size[0] + 250 + ghost_y, player_z]
    if key == b'p':
        if game:
            game = False
            print("Game paused")
        else:
            game = True
            print("Game resumed")
    if key == b'u':
        if debug_mode:
            debug_mode = False
            print("Debug mode OFF")
        else:
            debug_mode = True
            print("Debug mode ON")
    if debug_mode and key == b't':
        if stealth_mode:
            stealth_mode = False
            print("Stealth mode OFF")
        else:
            stealth_mode = True
            print("Stealth mode ON")
    if debug_mode and key == b'k' or key == b'K':
        # Cycle power level from 1 to 3 for testing
        power_level = (power_level % 3) + 1
        print(f"Power level is now {power_level}")
    if not game:
        if key == b',':
            camera_pos[2] -= cam_speed
        if key == b'.':
            camera_pos[2] += cam_speed
    glutPostRedisplay()

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
    global secondary_fire, bullets, player_pos, power_level
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        px = player_pos[0]
        py = player_pos[1] + 50
        pz = player_pos[2]

        if power_level == 1:
            # Level 1: Single straight bullet
            bullets.append([px, py, pz, 0.0, bullet_speed])
        elif power_level == 2:
            # Level 2: Dual parallel bullets
            bullets.append([px - 25, py, pz, 0.0, bullet_speed])
            bullets.append([px + 25, py, pz, 0.0, bullet_speed])
        elif power_level >= 3:
            # Level 3: Triple spread bullets (left angled, straight, right angled)
            bullets.append([px - 20, py, pz, -4.0, bullet_speed])
            bullets.append([px, py, pz, 0.0, bullet_speed])
            bullets.append([px + 20, py, pz, 4.0, bullet_speed])

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

def idle():
    global camera_pos, backup_cam, player_y, player_pos, camera_lock, cam_offset_y, cam_offset_z, map_y_size, ghost_y, max_player_y, min_player_y, rotor_angle, bullets, enemies
    if game:
        player_y += player_scene_speed
        ghost_y += player_scene_speed
        max_player_y += player_scene_speed
        min_player_y += player_scene_speed
        player_pos[1] = map_y_size[0] + 250 + player_y
        rotor_angle += rotor_turn_speed

        # Update active bullets (accounting for both vx and vy)
        for b in bullets:
            b[0] += b[3]  # x position += vx
            b[1] += b[4]  # y position += vy

        # Remove bullets that exceed bounds ahead
        bullets = [b for b in bullets if b[1] < player_pos[1] + 2000]

        # Update enemies
        update_enemies()

        # Check bullet-enemy collisions
        for i in range(len(bullets) - 1, -1, -1):
            for j in range(len(enemies) - 1, -1, -1):
                bx, by, bz = bullets[i][0], bullets[i][1], bullets[i][2]
                ex, ey, ez = enemies[j][0], enemies[j][1], enemies[j][2]
                # Simple distance check for collision
                if abs(bx - ex) < 30 and abs(by - ey) < 30 and abs(bz - ez) < 30:
                    bullets.pop(i)
                    defeat_enemy(j)
                    break

        camera_pos = [0, map_y_size[0] + cam_offset_y + ghost_y, cam_offset_z]
        camera_lock = [0, map_y_size[0] + 250 + ghost_y, player_z]

    if not game:
        backup_cam = [0, map_y_size[0] + cam_offset_y + ghost_y, cam_offset_z]
    glutPostRedisplay()

def spawn_enemy():
    global enemy_spawn_index
    x = enemy_spawn_x[enemy_spawn_index]
    y = player_pos[1] + 1500
    z = 250
    enemies.append([x, y, z])
    enemy_spawn_index += 1
    if enemy_spawn_index >= len(enemy_spawn_x):
        enemy_spawn_index = 0

def draw_enemy_airplane(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(-90, 0, 0, 1)
    glScalef(0.5, 0.5, 0.5)
    glPushMatrix()
    glColor3f(0.8, 0.1, 0.1)
    glScalef(120, 35, 30)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.6, 0.1, 0.1)
    glScalef(45, 180, 10)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.5, 0.05, 0.05)
    glTranslatef(-50, 0, 30)
    glScalef(40, 15, 60)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.6, 0.1, 0.1)
    glTranslatef(-50, 0, 0)
    glScalef(35, 90, 8)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.1, 0.3, 0.6)
    glTranslatef(25, 0, 22)
    glScalef(30, 25, 15)
    glutSolidCube(1)
    glPopMatrix()
    glPopMatrix()

def draw_enemies():
    for enemy in enemies:
        draw_enemy_airplane(enemy[0], enemy[1], enemy[2])

def update_enemies():
    for i in range(len(enemies) - 1, -1, -1):
        enemies[i][1] -= enemy_speed
        if enemies[i][1] < player_pos[1] - 500:
            enemies.pop(i)
            spawn_enemy()

def defeat_enemy(enemy_index):
    global score
    if enemy_index >= 0 and enemy_index < len(enemies):
        enemies.pop(enemy_index)
        score += 10
        spawn_enemy()

def draw_bullets():
    global bullets
    quadric = gluNewQuadric()
    for b in bullets:
        glPushMatrix()
        glTranslatef(b[0], b[1], b[2])
        # Rotate cylinder to point forward along the Y-axis
        glRotatef(90, 1, 0, 0)

        # Rocket Body (Cylinder)
        glColor3f(1.0, 0.3, 0.1)  # Fiery orange-red
        gluCylinder(quadric, 4, 4, 30, 8, 8)

        # Rocket Tip (Cone)
        glPushMatrix()
        glTranslatef(0, 0, 30)
        glColor3f(1.0, 1.0, 0.2)  # Bright yellow tip
        gluCylinder(quadric, 4, 0.5, 12, 8, 8)
        glPopMatrix()

        glPopMatrix()

def level_1():
    draw_tiles(tiles)
    for i in house_positions:
        draw_house(i[0], i[1], i[2])
    for i in garage_positions:
        draw_garage(i[0], i[1], i[2])
    for i in tree_positions:
        draw_tree(i[0], i[1], i[2])

    draw_bullets()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, window_width, window_height)
    setupCamera()

    if current_level == 1:
        level_1()

    draw_helicopter()
    draw_enemies()

    if stealth_mode:
        stealth_status = "ON"
    else:
        stealth_status = "OFF"

    glColor3f(0, 0, 0)
    draw_text(text_indent_x-2, window_height-text_indent_y-2, f"Health: {health}")
    draw_text(text_indent_x-2, window_height-2*text_indent_y-2, f"Score: {score}")
    draw_text(text_indent_x-2, window_height-3*text_indent_y-2, f"Lives: {lives}")
    draw_text(text_indent_x-2, window_height-4*text_indent_y-2, f"Power Lvl: {power_level}")
    draw_text(text_indent_x-2, window_height-5*text_indent_y-2, f"Stealth: {stealth_status}")

    glColor3f(1, 1, 1)
    draw_text(text_indent_x, window_height-text_indent_y, f"Health: {health}")
    draw_text(text_indent_x, window_height-2*text_indent_y, f"Score: {score}")
    draw_text(text_indent_x, window_height-3*text_indent_y, f"Lives: {lives}")
    draw_text(text_indent_x, window_height-4*text_indent_y, f"Power Lvl: {power_level}")
    draw_text(text_indent_x, window_height-5*text_indent_y, f"Stealth: {stealth_status}")

    if not game:
        glColor3f(0, 0, 0)
        draw_text(window_width/2-2, window_height/2-2, f"Pause")
        glColor3f(1, 1, 1)
        draw_text(window_width/2, window_height/2, f"Pause")
    if game_over:
        glColor3f(0,0,0)
        draw_text(window_width/2-2, window_height/2-2, f"Game Over!")
        glColor3f(1,1,1)
        draw_text(window_width/2, window_height/2, f"Game Over!")
    glutSwapBuffers()

def draw_terrain(x_start, y_start, columns, rows, tile_size, color_range, z, misc):
    global tiles
    z_array = []
    backup_z_array = []
    for y in range(rows):
        z_array = []
        Z1, Z2, Z3, Z4 = 0, 0, 0, 0
        for x in range(columns):
            r = random.uniform(color_range[0][0], color_range[0][1])
            g = random.uniform(color_range[1][0], color_range[1][1])
            b = random.uniform(color_range[2][0], color_range[2][1])
            if x == 0 and y == 0 and misc == []:
                Z1 = random.randint(z[0], z[1])
                Z2 = random.randint(z[0], z[1])
                Z3 = random.randint(z[0], z[1])
                Z4 = random.randint(z[0], z[1])
            elif y == 0 and misc == []:
                Z1 = Z4
                Z2 = Z3
                Z3 = random.randint(z[0], z[1])
                Z4 = random.randint(z[0], z[1])
            elif x == 0 and y == 0:
                Z1 = misc[x][0]
                Z2 = random.randint(z[0], z[1])
                Z3 = random.randint(z[0], z[1])
                Z4 = misc[x][1]
            elif y == 0:
                Z1 = Z4
                Z2 = Z3
                Z3 = random.randint(z[0], z[1])
                Z4 = misc[x][1]
            elif x == 0:
                Z1 = backup_z_array[x][0]
                Z2 = random.randint(z[0], z[1])
                Z3 = random.randint(z[0], z[1])
                Z4 = backup_z_array[x][1]
            else:
                Z1 = Z4
                Z2 = Z3
                Z3 = random.randint(z[0], z[1])
                Z4 = backup_z_array[x][1]
            z_array.append([Z2, Z3])
            tiles.append([x_start, x, y_start, y, tile_size, r, g, b, Z1, Z2, Z3, Z4])
        backup_z_array = z_array.copy()
    misc = backup_z_array.copy()
    return misc

def draw_tiles(tile):
    glBegin(GL_QUADS)
    for i in tile:
        x_start = i[0]
        x = i[1]
        y_start = i[2]
        y = i[3]
        tile_size = i[4]
        r = i[5]
        g = i[6]
        b = i[7]
        Z1 = i[8]
        Z2 = i[9]
        Z3 = i[10]
        Z4 = i[11]
        glColor3f(r, g, b)
        glVertex3f(x_start + x * tile_size, y_start + y * tile_size, Z1)
        glVertex3f(x_start + x * tile_size, y_start + (y+1) * tile_size, Z2)
        glVertex3f(x_start + (x+1) * tile_size, y_start + (y+1) * tile_size, Z3)
        glVertex3f(x_start + (x+1) * tile_size, y_start + y * tile_size, Z4)
    glEnd()

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
    glScalef(1.5, 1.5, 1)
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

def draw_garage(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(90, 1, 0, 0)
    glPushMatrix()
    glColor3f(0.75, 0.7, 0.6)
    glScalef(120, 100, 100)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.4, 0.35, 0.3)
    glTranslatef(0, 0, 51)
    glScalef(80, 70, 5)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.55, 0.3, 0.2)
    glTranslatef(0, 55, 0)
    glScalef(130, 15, 110)
    glutSolidCube(1)
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
    glColor3f(0.4, 0.25, 0.1)
    glTranslatef(0, -30, 61)
    glScalef(40, 70, 5)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.7, 0.85, 0.95)
    glTranslatef(-60, 20, 61)
    glScalef(35, 35, 5)
    glutSolidCube(1)
    glPopMatrix()
    glPopMatrix()

def draw_helicopter():
    global player_pos, rotor_angle, stealth_mode
    quadric = gluNewQuadric()

    def heli_color(r, g, b):
        if stealth_mode:
            glColor3f(0.8, 0.9, 1.0)
        else:
            glColor3f(r, g, b)

    glPushMatrix()
    glTranslatef(player_pos[0], player_pos[1], player_pos[2])
    glScalef(0.7, 0.7, 0.7)
    glRotatef(helicopter_angle, 0, 0, 1)
    glRotatef(helicopter_tilt, 1, 0, 0)

    glPushMatrix()
    heli_color(0.15, 0.15, 0.18)
    glTranslatef(0, 0, 120)
    glScalef(2.2, 1.2, 1.0)
    gluSphere(quadric, 60, 10, 10)
    glPopMatrix()

    glPushMatrix()
    heli_color(0.1, 0.6, 0.9)
    glTranslatef(0, -45, 130)
    glScalef(1.5, 0.8, 0.7)
    gluSphere(quadric, 45, 10, 10)
    glPopMatrix()

    glPushMatrix()
    heli_color(0.05, 0.4, 0.7)
    glTranslatef(0, 40, 130)
    glScalef(1.5, 0.8, 0.7)
    gluSphere(quadric, 45, 10, 10)
    glPopMatrix()

    glPushMatrix()
    heli_color(0.15, 0.15, 0.18)
    glTranslatef(110, 0, 135)
    glRotatef(90, 0, 1, 0)
    gluCylinder(quadric, 25, 10, 190, 10, 10)
    glPopMatrix()

    glPushMatrix()
    heli_color(0.15, 0.15, 0.18)
    glTranslatef(300, 0, 135)
    glScalef(0.5, 0.5, 0.8)
    gluSphere(quadric, 25, 10, 10)
    glPopMatrix()

    glPushMatrix()
    heli_color(0.1, 0.1, 0.1)
    glTranslatef(0, 0, 180)
    gluCylinder(quadric, 8, 8, 30, 10, 10)
    glPopMatrix()

    glPushMatrix()
    heli_color(0.05, 0.05, 0.05)
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
    heli_color(0.25, 0.25, 0.25)
    glTranslatef(-25, -55, 60)
    glScalef(1.8, 0.12, 0.12)
    glutSolidCube(40)
    glPopMatrix()

    glPushMatrix()
    heli_color(0.25, 0.25, 0.25)
    glTranslatef(-25, 55, 60)
    glScalef(1.8, 0.12, 0.12)
    glutSolidCube(40)
    glPopMatrix()

    glPushMatrix()
    heli_color(0.25, 0.25, 0.25)
    glTranslatef(-30, -45, 85)
    glScalef(0.12, 0.12, 0.6)
    glutSolidCube(40)
    glPopMatrix()

    glPushMatrix()
    heli_color(0.25, 0.25, 0.25)
    glTranslatef(30, -45, 85)
    glScalef(0.12, 0.12, 0.6)
    glutSolidCube(40)
    glPopMatrix()

    glPushMatrix()
    heli_color(0.25, 0.25, 0.25)
    glTranslatef(-30, 45, 85)
    glScalef(0.12, 0.12, 0.6)
    glutSolidCube(40)
    glPopMatrix()

    glPushMatrix()
    heli_color(0.25, 0.25, 0.25)
    glTranslatef(30, 45, 85)
    glScalef(0.12, 0.12, 0.6)
    glutSolidCube(40)
    glPopMatrix()

    glPopMatrix()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_width, window_height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Air Strike")

    # Initialize some enemies
    for _ in range(5):
        spawn_enemy()

    if current_level == 1:
        backup = draw_terrain(map_x_size[0], map_y_size[0] - 1000, columns[0], 5, tile_size, [[0.6, 0.7], [0.8, 1], [0, 0]], [-20, 20], [])
        hello = draw_terrain(map_x_size[0], map_y_size[0], columns[0], rows[0], tile_size, [[0.6, 0.7], [0.8, 1], [0, 0]], [-20, 20], backup)
    print("Game Start!")
    glutDisplayFunc(showScreen)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)

    glutMainLoop()

if __name__ == "__main__":
    main()