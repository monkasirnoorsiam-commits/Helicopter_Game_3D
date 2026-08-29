bullets = []
bullet_speed = 35
bullet_limit = 3000


def fire_bullet():

    bullets.append([
        player_pos[0],
        player_pos[1] + 120,
        player_pos[2] + 80
    ])

def draw_bullet(x, y, z):

    glPushMatrix()

    glTranslatef(x, y, z)

    glColor3f(1, 1, 0)

    gluSphere(
        gluNewQuadric(),
        12,
        10,
        10
    )

    glPopMatrix()


def draw_bullets():

    for bullet in bullets:

        draw_bullet(
            bullet[0],
            bullet[1],
            bullet[2]
        )

def update_bullets():

    global bullets

    remaining_bullets = []

    for bullet in bullets:

        # Move bullet forward
        bullet[1] += bullet_speed

        # Keep bullet until it travels too far
        if bullet[1] < player_pos[1] + bullet_limit:

            remaining_bullets.append(bullet)

    bullets = remaining_bullets