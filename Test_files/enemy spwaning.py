enemies = []

enemy_speed = 2

enemy_spawn_x = [
    -500,
    -250,
    0,
    250,
    500
]

enemy_spawn_index = 0


# =====================================================
# SPAWN ENEMY
# =====================================================

def spawn_enemy():

    global enemy_spawn_index

    x = enemy_spawn_x[enemy_spawn_index]
    y = player_pos[1] + 1500
    z = 250

    enemies.append([x, y, z])

    enemy_spawn_index += 1

    if enemy_spawn_index >= len(enemy_spawn_x):
        enemy_spawn_index = 0


# =====================================================
# DRAW ENEMY AIRPLANE
# =====================================================

def draw_enemy_airplane(x, y, z):

    glPushMatrix()

    glTranslatef(x, y, z)

    glRotatef(-90, 0, 0, 1)

    glScalef(0.5, 0.5, 0.5)


    # Main body
    glPushMatrix()
    glColor3f(0.8, 0.1, 0.1)
    glScalef(120, 35, 30)
    glutSolidCube(1)
    glPopMatrix()


    # Main wings
    glPushMatrix()
    glColor3f(0.6, 0.1, 0.1)
    glScalef(45, 180, 10)
    glutSolidCube(1)
    glPopMatrix()


    # Tail
    glPushMatrix()
    glColor3f(0.5, 0.05, 0.05)
    glTranslatef(-50, 0, 30)
    glScalef(40, 15, 60)
    glutSolidCube(1)
    glPopMatrix()


    # Back wings
    glPushMatrix()
    glColor3f(0.6, 0.1, 0.1)
    glTranslatef(-50, 0, 0)
    glScalef(35, 90, 8)
    glutSolidCube(1)
    glPopMatrix()


    # Cockpit
    glPushMatrix()
    glColor3f(0.1, 0.3, 0.6)
    glTranslatef(25, 0, 22)
    glScalef(30, 25, 15)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()


# =====================================================
# DRAW ALL ENEMIES
# =====================================================

def draw_enemies():

    for enemy in enemies:
        draw_enemy_airplane(enemy[0], enemy[1], enemy[2])


# =====================================================
# UPDATE / RESPAWN ENEMIES
# =====================================================

def update_enemies():

    for i in range(len(enemies) - 1, -1, -1):

        enemies[i][1] -= enemy_speed

        # if enemy goes behind player, remove and respawn
        if enemies[i][1] < player_pos[1] - 500:
            enemies.pop(i)
            spawn_enemy()


# =====================================================
# REMOVE DESTROYED ENEMY AND SPAWN NEW ONE
# =====================================================

def defeat_enemy(enemy_index):

    global score

    if enemy_index >= 0 and enemy_index < len(enemies):
        enemies.pop(enemy_index)
        score += 10
        spawn_enemy()