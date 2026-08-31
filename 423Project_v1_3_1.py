from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

window_height = 800
window_width = 1000
text_indent_x = 10
text_indent_y = 30
map_y_size = [-15000, -15000, -15000]
map_x_size = [-2000, -2000, -2000]
win_y_size = [400, 400, 400]
house_positions1 = [
    [-500, 500, 0], [400, -500, 0], [-200, -1500, 0], [600, 1000, 0], [-400, 1600, 0], [300, -1000, 0], [-100, 1000, 0], [500, 0, 0],
    [-800, -3000, 0], [1000, -4000, 0], [-1200, -5000, 0], [1400, -6000, 0], [-600, -7000, 0], [800, -8000, 0], [-1000, -9000, 0], [1200, -10000, 0],
    [-400, -11000, 0], [600, -12000, 0], [-800, -13000, 0], [1000, -14000, 0], [-1200, -15000, 0], [1400, -16000, 0], [-200, 800, 0], [200, -17000, 0]
]
garage_positions1 = [
    [-300, 500, 0], [650, -500, 0], [-100, -1500, 0], [700, 1000, 0], [-500, 1600, 0], [450, -1000, 0], [-150, 1000, 0], [600, 0, 0],
    [-700, -3500, 0], [1100, -4500, 0], [-1300, -5500, 0], [1500, -6500, 0], [-500, -7500, 0], [900, -8500, 0], [-1100, -9500, 0], [1300, -10500, 0],
    [-300, -11500, 0], [700, -12500, 0], [-900, -13500, 0], [1100, -14500, 0], [-1300, -15500, 0], [1500, -16500, 0], [-100, 500, 0], [300, -13000, 0]
]
tree_positions1 = [
    [-300, 100, 0], [-200, 900, 0], [600, -1000, 0], [200, -200, 0], [-400, -1800, 0], [500, 1200, 0], [-600, 1600, 0], [400, -1200, 0],
    [-100, 700, 0], [700, -300, 0], [-450, 200, 0], [250, -800, 0], [-350, 1500, 0], [550, 300, 0], [-50, -1700, 0], [650, 1300, 0],
    [-900, -2500, 0], [850, -3200, 0], [-700, -3800, 0], [750, -4500, 0], [-1100, -5200, 0], [1050, -5800, 0], [-650, -6500, 0], [950, -7200, 0],
    [-1250, -7900, 0], [1150, -8600, 0], [-550, -9300, 0], [850, -10000, 0], [-1150, -10700, 0], [1350, -11400, 0], [-450, -12100, 0], [750, -12800, 0],
    [-1050, -13500, 0], [1250, -14200, 0], [-350, -14900, 0], [650, -15600, 0], [-950, -16300, 0], [1450, -16800, 0], [-150, -17500, 0], [550, -18200, 0],
    [-1350, 800, 0], [1300, 200, 0], [-250, -400, 0], [200, -1000, 0], [-1100, -1600, 0], [1000, -2200, 0], [-150, -2800, 0], [150, -3400, 0],
    [-1400, -4000, 0], [1400, -4600, 0], [-200, -5200, 0], [100, -5800, 0], [-1300, -6400, 0], [1200, -7000, 0], [-100, -7600, 0], [50, -8200, 0],
    [-1450, -8800, 0], [1450, -9400, 0], [-50, -10000, 0], [0, -10600, 0], [-1200, -11200, 0], [1100, -11800, 0], [-30, -12400, 0], [70, -13000, 0],
    [-1400, -13600, 0], [1350, -14200, 0], [-40, -14800, 0], [60, -15400, 0], [-1150, -16000, 0], [1300, -16600, 0], [-20, -17200, 0], [80, -17800, 0]
]
house_positions2 = [
    [-500, 0, 0], [400, -1000, 0], [-300, -2000, 0], [600, 1000, 0], [-400, 1600, 0], [300, -1500, 0],
    [-800, -3500, 0], [1000, -4500, 0], [-1200, -5500, 0], [1400, -6500, 0], [-600, -7500, 0], [800, -8500, 0],
    [-400, -11500, 0], [600, -12500, 0], [-800, -13500, 0], [1000, -14500, 0], [-1200, -15500, 0], [1400, -16500, 0],
    [-200, 500, 0], [200, -17500, 0]
]
garage_positions2 = [
    [-300, 200, 0], [650, -800, 0], [-100, -1800, 0], [700, 1200, 0], [-500, 1600, 0], [450, -1300, 0],
    [-700, -3800, 0], [1100, -4800, 0], [-1300, -5800, 0], [1600, -6800, 0], [-500, -7800, 0], [900, -8800, 0],
    [-300, -11800, 0], [700, -12800, 0], [-900, -13800, 0], [1100, -14800, 0], [-1300, -15800, 0], [1600, -16800, 0],
    [-150, 200, 0], [350, -12800, 0]
]
tree_positions2 = [
    [-250, 0, 0], [-150, 800, 0], [550, -1100, 0], [150, -300, 0], [-350, -1900, 0], [450, 1100, 0], [-550, 1600, 0], [350, -1300, 0],
    [-50, 600, 0], [650, -400, 0], [-400, 100, 0], [200, -1000, 0], [-300, 1400, 0], [500, 200, 0], [0, -1800, 0], [600, 1300, 0],
    [-850, -2600, 0], [800, -3300, 0], [-650, -3900, 0], [700, -4600, 0], [-1050, -5300, 0], [1000, -5900, 0], [-600, -6600, 0], [900, -7300, 0],
    [-1200, -8000, 0], [1100, -8700, 0], [-500, -9400, 0], [800, -10100, 0], [-1100, -10800, 0], [1300, -11500, 0], [-400, -12200, 0], [700, -12900, 0],
    [-1000, -13600, 0], [1200, -14300, 0], [-300, -15000, 0], [600, -15700, 0], [-900, -16400, 0], [1400, -16900, 0], [-100, -17600, 0], [500, -18300, 0],
    [-1300, 700, 0], [1250, 100, 0], [-200, -700, 0], [150, -1300, 0], [-1050, -1900, 0], [950, -2500, 0], [-100, -3100, 0], [100, -3700, 0],
    [-1350, -4100, 0], [1350, -4700, 0], [-150, -5300, 0], [50, -5900, 0], [-1250, -6500, 0], [1150, -7100, 0], [-50, -7700, 0], [0, -8300, 0],
    [-1400, -8900, 0], [1400, -9500, 0], [0, -10100, 0], [-10, -10700, 0], [-1150, -11300, 0], [1050, -11900, 0], [-20, -12500, 0], [60, -13100, 0],
    [-1350, -13700, 0], [1300, -14300, 0], [-30, -14900, 0], [50, -15500, 0], [-1100, -16100, 0], [1250, -16700, 0], [-10, -17300, 0], [70, -17900, 0],
    [-280, -100, 0], [-180, 700, 0], [580, -1200, 0], [180, -400, 0], [-380, -2000, 0], [480, 1000, 0], [-580, 1600, 0], [380, -1350, 0],
    [-80, 550, 0], [680, -450, 0], [-430, 50, 0], [230, -950, 0], [-330, 1350, 0], [530, 250, 0], [30, -1850, 0], [630, 1350, 0]
]
house_positions3 = [
    [-550, -200, 0], [450, -1200, 0], [-350, -2200, 0], [650, 800, 0], [-450, 1600, 0], [350, -1700, 0],
    [-850, -4000, 0], [1050, -5000, 0], [-1350, -6000, 0], [1550, -7000, 0], [-650, -8000, 0], [850, -9000, 0],
    [-450, -12500, 0], [650, -13500, 0], [-850, -14500, 0], [1050, -15500, 0], [-1350, -16500, 0], [1550, -17500, 0],
    [-250, 300, 0], [250, -18500, 0]
]
garage_positions3 = [
    [-400, 0, 0], [750, -1000, 0], [-250, -2000, 0], [800, 1000, 0], [-600, 1600, 0], [550, -1500, 0],
    [-800, -4500, 0], [1200, -5500, 0], [-1500, -6500, 0], [1800, -7500, 0], [-600, -8500, 0], [1000, -9500, 0],
    [-400, -13000, 0], [800, -14000, 0], [-1000, -15000, 0], [1200, -16000, 0], [-1500, -17000, 0], [1800, -18000, 0],
    [-200, 100, 0], [400, -14500, 0]
]
tree_positions3 = [
    [-350, -100, 0], [-250, 700, 0], [650, -1200, 0], [250, -400, 0], [-450, -2000, 0], [550, 1000, 0], [-650, 1600, 0], [450, -1400, 0],
    [-950, -2700, 0], [900, -3400, 0], [-750, -4000, 0], [800, -4700, 0], [-1150, -5400, 0], [1100, -6000, 0], [-700, -6700, 0], [1000, -7400, 0],
    [-1300, -8100, 0], [1200, -8800, 0], [-600, -9500, 0], [900, -10200, 0], [-1200, -10900, 0], [1400, -11600, 0], [-500, -12300, 0], [800, -13000, 0],
    [-1100, -13700, 0], [1300, -14400, 0], [-400, -15100, 0], [700, -15800, 0], [-1000, -16500, 0], [1500, -17200, 0], [-200, -17900, 0], [600, -18600, 0],
    [-1400, 600, 0], [1350, 0, 0], [-300, -600, 0], [250, -1200, 0], [-1150, -1800, 0], [1050, -2400, 0], [-200, -3000, 0], [200, -3600, 0],
    [-1450, -4200, 0], [1450, -4800, 0], [-250, -5400, 0], [150, -6000, 0], [-1350, -6600, 0], [1250, -7200, 0], [-150, -7800, 0], [100, -8400, 0],
    [-1500, -9000, 0], [1500, -9600, 0], [-100, -10200, 0], [50, -10800, 0], [-1250, -11400, 0], [1150, -12000, 0], [-50, -12600, 0], [100, -13200, 0],
    [-1450, -13800, 0], [1400, -14400, 0], [-50, -15000, 0], [100, -15600, 0], [-1200, -16200, 0], [1350, -16800, 0], [-50, -17400, 0], [120, -18000, 0],
    [-380, -200, 0], [-280, 600, 0], [680, -1300, 0], [280, -500, 0], [-480, -2100, 0], [580, 1100, 0], [-680, 1600, 0], [480, -1450, 0],
    [-180, 500, 0], [780, -500, 0], [-530, 0, 0], [330, -1000, 0], [-430, 1300, 0], [630, 200, 0], [130, -1850, 0], [730, 1300, 0]
]
columns = [20, 20, 20]
rows = [90, 90, 90]
tile_size = 200
tiles = []
color_range = [[[0.6, 0.7], [0.8, 1], [0, 0]], [[0.9, 1], [0.8, 0.95], [0, 0.1]], [[0.75, 0.9], [0.2, 0.35], [0, 0]]]

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
zFar = 1300

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
lives = 3
player_scene_speed = 1
level_complete = False
game_complete = False
prompt = False

enemies = []
enemy_speed = 2

enemy_bullets = []
enemy_bullet_speed = 12
enemy_fire_distance = 700

debug_mode = False
stealth_mode = False
power_level = 1
bullets = []
bullet_speed = 30

def restart_game():
    global health, score, lives, power_level, player_y, player_x, ghost_y, bullets, enemies, enemy_bullets, stealth_mode, game_over, game, player_pos, camera_pos, camera_lock, ghost_pos, min_player_y, max_player_y, min_player_x, max_player_x, rotor_angle

    health = 100
    score = 0
    lives = 3
    power_level = 1
    player_y = 0
    player_x = 0
    ghost_y = 0
    bullets = []
    enemies = []
    enemy_bullets = []
    stealth_mode = False
    game_over = False
    game = True
    rotor_angle = 0

    min_player_y = -400
    max_player_y = 300
    min_player_x = -600
    max_player_x = 600

    player_pos = [player_x, map_y_size[0] + player_y, player_z]
    ghost_pos = [player_x, map_y_size[0] + ghost_y, player_z]
    camera_pos = [0, map_y_size[0] + cam_offset_y + ghost_y, cam_offset_z]
    camera_lock = [0, map_y_size[0] + 250 + ghost_y, player_z]

    for _ in range(5):
        spawn_enemy()

    regenerate_tiles()

    print("Game Start!")

def keyboardListener(key, x, y):
    global prompt, player_scene_speed, zFar, current_level, debug_mode, player_pos, game, camera_pos, cam_speed, player_x, player_y, camera_lock, cam_offset_y, cam_offset_z, map_y_size, max_player_x, min_player_x, max_player_y, min_player_y, stealth_mode, power_level, enemies, rotor_angle
    if game:
        if key == b'w' or key == b'W':
            if player_y < max_player_y:
                player_y += player_speed
                player_pos[1] += player_speed
            else:
                player_y = max_player_y
                player_pos[1] = max_player_y
        if key == b's' or key == b'S':
            if player_y > min_player_y:
                player_y -= player_speed
                player_pos[1] -= player_speed
            else:
                player_y = min_player_y
                player_pos[1] = min_player_y
        if key == b'a' or key == b'A':
            if player_x > min_player_x:
                player_x -= player_speed
                player_pos[0] -= player_speed
            else:
                player_x = min_player_x
                player_pos[0] = min_player_x
        if key == b'd' or key == b'D':
            if player_x < max_player_x:
                player_x += player_speed
                player_pos[0] += player_speed
            else:
                player_x = max_player_x
                player_pos[0] = max_player_x
        camera_pos = [0, map_y_size[0] + cam_offset_y + ghost_y, cam_offset_z]
        camera_lock = [0, map_y_size[0] + 250 + ghost_y, player_z]
    if (key == b'p' or key == b'P') and not game_over:
        if game:
            game = False
            zFar = 3000
            print("Game paused")
        else:
            game = True
            zFar = 1300
            print("Game resumed")
    if (level_complete or game_complete) and key == b' ':
        prompt = True
    if key == b'u' or key == b'U':
        if debug_mode:
            debug_mode = False
            print("Debug mode OFF")
        else:
            debug_mode = True
            print("Debug mode ON")
    if debug_mode and (key == b't' or key == b'T'):
        if stealth_mode:
            stealth_mode = False
            print("Stealth mode OFF")
        else:
            stealth_mode = True
            print("Stealth mode ON")
    if debug_mode and (key == b'k' or key == b'K'):
        power_level = (power_level % 4) + 1
        print(f"Power level is now {power_level}")
    if debug_mode and (key == b'l' or key == b'L'):
        current_level = (current_level % 3) + 1
        regenerate_tiles()
        print(f"Level {current_level}")
    if key == b'r' or key == b'R':
        restart_game()
    if debug_mode and key == b'[':
        player_scene_speed -= 0.1
    if debug_mode and key == b']':
        player_scene_speed += 0.1
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
            bullets.append([px, py, pz, 0.0, bullet_speed])
        elif power_level == 2:
            bullets.append([px - 25, py, pz, 0.0, bullet_speed])
            bullets.append([px + 25, py, pz, 0.0, bullet_speed])
        elif power_level == 3:
            bullets.append([px - 20, py, pz, -4.0, bullet_speed])
            bullets.append([px, py, pz, 0.0, bullet_speed])
            bullets.append([px + 20, py, pz, 4.0, bullet_speed])
        elif power_level == 4:
            bullets.append([px - 50, py, pz, -7.0, bullet_speed])
            bullets.append([px - 20, py, pz, -4.0, bullet_speed])
            bullets.append([px, py, pz, 0.0, bullet_speed])
            bullets.append([px + 20, py, pz, 4.0, bullet_speed])
            bullets.append([px + 50, py, pz, 7.0, bullet_speed])

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
    global score, lives, prompt, current_level, win_y_size, ghost_pos, max_player_x, min_player_x, stealth_mode, power_level, game_complete, game, level_complete, camera_pos, backup_cam, player_y, player_pos, camera_lock, cam_offset_y, cam_offset_z, map_y_size, ghost_y, max_player_y, min_player_y, rotor_angle, bullets, enemies, enemy_bullets, health
    if game:
        player_y += player_scene_speed
        ghost_y += player_scene_speed
        max_player_y += player_scene_speed
        min_player_y += player_scene_speed
        player_pos[1] = map_y_size[0] + 250 + player_y
        rotor_angle += rotor_turn_speed

        for b in bullets:
            b[0] += b[3]
            b[1] += b[4]

        bullets = [b for b in bullets if b[1] < player_pos[1] + 2000]

        update_enemies()

        update_enemy_bullets()

        for i in range(len(bullets) - 1, -1, -1):
            for j in range(len(enemies) - 1, -1, -1):
                bx, by, bz = bullets[i][0], bullets[i][1], bullets[i][2]
                ex, ey, ez = enemies[j][0], enemies[j][1], enemies[j][2]
                if abs(bx - ex) < 60 and abs(by - ey) < 60 and abs(bz - ez) < 40:
                    bullets.pop(i)
                    defeat_enemy(j)
                    break

        camera_pos = [0, map_y_size[0] + cam_offset_y + ghost_y, cam_offset_z]
        camera_lock = [0, map_y_size[0] + 250 + ghost_y, player_z]

        if player_pos[1] >= win_y_size[current_level - 1]:
            if current_level != levels:
                level_complete = True
                game = False
            else:
                game_complete = True
                score = 0
                lives = 3
                game = False

    if not game:
        backup_cam = [0, map_y_size[0] + cam_offset_y + ghost_y, cam_offset_z]

    if prompt:
        game = True
        if current_level != levels:
            current_level += 1
        else:
            current_level = 1
        health = 100
        power_level = 1
        player_y = 0
        player_x = 0
        ghost_y = 0
        bullets = []
        enemies = []
        enemy_bullets = []
        stealth_mode = False

        min_player_y = -400
        max_player_y = 300
        min_player_x = -600
        max_player_x = 600

        player_pos = [player_x, map_y_size[0] + player_y, player_z]
        ghost_pos = [player_x, map_y_size[0] + ghost_y, player_z]
        camera_pos = [0, map_y_size[0] + cam_offset_y + ghost_y, cam_offset_z]
        camera_lock = [0, map_y_size[0] + 250 + ghost_y, player_z]

        for _ in range(5):
            spawn_enemy()

        # Regenerate tiles for the new level
        regenerate_tiles()

        level_complete = False
        game_complete = False
        prompt = False

    glutPostRedisplay()

def spawn_enemy():
    x = random.randint(-500, 500)
    y = player_pos[1] + random.randint(1200, 1800)
    z = player_pos[2]

    enemies.append([x, y, z, False])

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

def enemy_fire(enemy):
    enemy_bullets.append([enemy[0], enemy[1] - 50, enemy[2]])

def update_enemies():
    for i in range(len(enemies) - 1, -1, -1):
        enemies[i][1] -= enemy_speed

        distance = enemies[i][1] - player_pos[1]

        if distance < enemy_fire_distance and enemies[i][3] == False:
            enemy_fire(enemies[i])
            enemies[i][3] = True

        if enemies[i][1] < player_pos[1] - 500:
            enemies.pop(i)
            spawn_enemy()

def update_enemy_bullets():
    global health, lives, game_over, game

    for i in range(len(enemy_bullets) - 1, -1, -1):

        enemy_bullets[i][1] -= enemy_bullet_speed

        bx = enemy_bullets[i][0]
        by = enemy_bullets[i][1]
        bz = enemy_bullets[i][2]

        if (
            abs(bx - player_pos[0]) < 70
            and abs(by - player_pos[1]) < 70
            and abs(bz - player_pos[2]) < 70
        ):
            health -= 10
            enemy_bullets.pop(i)

            if health <= 0:
                lives -= 1

                if lives > 0:
                    health = 100

                else:
                    lives = 0
                    health = 0
                    game_over = True
                    game = False
                    return

        elif by < player_pos[1] - 500:
            enemy_bullets.pop(i)

def draw_enemy_bullets():
    for b in enemy_bullets:
        glPushMatrix()
        glTranslatef(b[0], b[1], b[2])
        glColor3f(1.0, 0.0, 0.0)
        gluSphere(gluNewQuadric(), 8, 8, 8)
        glPopMatrix()

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
        glRotatef(90, 1, 0, 0)

        glColor3f(1.0, 0.3, 0.1)
        gluCylinder(quadric, 4, 4, 30, 8, 8)

        glPushMatrix()
        glTranslatef(0, 0, 30)
        glColor3f(1.0, 1.0, 0.2)
        gluCylinder(quadric, 4, 0.5, 12, 8, 8)
        glPopMatrix()

        glPopMatrix()

def level_1():
    draw_tiles(tiles)
    for i in house_positions1:
        draw_house(i[0], i[1], i[2])
    for i in garage_positions1:
        draw_garage(i[0], i[1], i[2])
    for i in tree_positions1:
        draw_tree(i[0], i[1], i[2])

def level_2():
    draw_tiles(tiles)
    for i in house_positions2:
        draw_house(i[0], i[1], i[2])
    for i in garage_positions2:
        draw_garage(i[0], i[1], i[2])
    for i in tree_positions2:
        draw_tree(i[0], i[1], i[2])

def level_3():
    draw_tiles(tiles)
    for i in house_positions3:
        draw_house(i[0], i[1], i[2])
    for i in garage_positions3:
        draw_garage(i[0], i[1], i[2])
    for i in tree_positions3:
        draw_tree(i[0], i[1], i[2])

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, window_width, window_height)
    setupCamera()

    if current_level == 1:
        level_1()
    elif current_level == 2:
        level_2()
    elif current_level == 3:
        level_3()

    draw_bullets()
    draw_helicopter()
    draw_enemies()
    draw_enemy_bullets()

    if stealth_mode:
        stealth_status = "ON"
    else:
        stealth_status = "OFF"

    glColor3f(0, 0, 0)
    draw_text(text_indent_x-2, window_height-text_indent_y-2, f"Health: {health}")
    draw_text(text_indent_x-2, window_height-2*text_indent_y-2, f"Score: {score}")
    draw_text(text_indent_x-2, window_height-3*text_indent_y-2, f"Lives: {lives}")
    draw_text(text_indent_x-2, window_height-4*text_indent_y-2, f"Level: {current_level}")
    draw_text(text_indent_x-2, window_height-5*text_indent_y-2, f"Power: {power_level}")
    draw_text(text_indent_x-2, window_height-6*text_indent_y-2, f"Stealth: {stealth_status}")

    glColor3f(1, 1, 1)
    draw_text(text_indent_x, window_height-text_indent_y, f"Health: {health}")
    draw_text(text_indent_x, window_height-2*text_indent_y, f"Score: {score}")
    draw_text(text_indent_x, window_height-3*text_indent_y, f"Lives: {lives}")
    draw_text(text_indent_x, window_height-4*text_indent_y, f"Level: {current_level}")
    draw_text(text_indent_x, window_height-5*text_indent_y, f"Power: {power_level}")
    draw_text(text_indent_x, window_height-6*text_indent_y, f"Stealth: {stealth_status}")
    if level_complete and not game:
        glColor3f(0, 0, 0)
        draw_text(window_width/2-2-text_indent_y*2.5, window_height/2-2, f"Level Complete!")
        glColor3f(1, 1, 1)
        draw_text(window_width/2-text_indent_y*2.5, window_height/2, f"Level Complete!")
        glColor3f(0, 0, 0)
        draw_text(window_width/3-2, window_height/2-text_indent_y-2, f"Press Space to proceed to next level")
        glColor3f(1, 1, 1)
        draw_text(window_width/3, window_height/2-text_indent_y, f"Press Space to proceed to next level")
    elif game_complete and not game:
        glColor3f(0, 0, 0)
        draw_text(window_width/2-2-text_indent_y*2.5, window_height/2-2, f"Congratulations!")
        glColor3f(1, 1, 1)
        draw_text(window_width/2-text_indent_y*2.5, window_height/2, f"Congratulations!")
        glColor3f(0, 0, 0)
        draw_text(window_width/3-2, window_height/2-text_indent_y-2, f"You have completed the game")
        glColor3f(1, 1, 1)
        draw_text(window_width/3, window_height/2-text_indent_y, f"You have completed the game")
        glColor3f(0, 0, 0)
        draw_text(window_width/2-2-text_indent_y*2.5, window_height/2-text_indent_y*2-2, f"Score {score}")
        glColor3f(1, 1, 1)
        draw_text(window_width/2-2-text_indent_y*2.5, window_height/2-text_indent_y*2, f"Score {score}")
    elif not game:
        glColor3f(0, 0, 0)
        draw_text(window_width/2-2, window_height/2-2, f"Pause")
        glColor3f(1, 1, 1)
        draw_text(window_width/2, window_height/2, f"Pause")
    elif game_over:
        glColor3f(0,0,0)
        draw_text(window_width/2-2, window_height/2-2, f"Game Over!")
        glColor3f(1,1,1)
        draw_text(window_width/2, window_height/2, f"Game Over!")
    elif debug_mode:
        glColor3f(0,0,0)
        draw_text(text_indent_x-2, window_height-7*text_indent_y-2, f"Debug Mode ON")
        glColor3f(1,1,1)
        draw_text(text_indent_x, window_height-7*text_indent_y, f"Debug Mode ON")
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

def regenerate_tiles():
    global tiles, current_level
    tiles = []
    if current_level == 1:
        backup = draw_terrain(map_x_size[0], map_y_size[0] - 1000, columns[0], 5, tile_size, color_range[0], [-20, 20], [])
        hello = draw_terrain(map_x_size[0], map_y_size[0], columns[0], rows[0], tile_size, color_range[0], [-20, 20], backup)
    elif current_level == 2:
        backup = draw_terrain(map_x_size[0], map_y_size[0] - 1000, columns[0], 5, tile_size, color_range[1], [-20, 20], [])
        hello = draw_terrain(map_x_size[0], map_y_size[0], columns[0], rows[0], tile_size, color_range[1], [-20, 20], backup)
    elif current_level == 3:
        backup = draw_terrain(map_x_size[0], map_y_size[0] - 1000, columns[0], 5, tile_size, color_range[2], [-20, 20], [])
        hello = draw_terrain(map_x_size[0], map_y_size[0], columns[0], rows[0], tile_size, color_range[2], [-20, 20], backup)

def main():
    global tiles
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_width, window_height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Air Strike")

    for _ in range(5):
        spawn_enemy()

    regenerate_tiles()
    print("Game Start!")
    glutDisplayFunc(showScreen)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)

    glutMainLoop()

if __name__ == "__main__":
    main()