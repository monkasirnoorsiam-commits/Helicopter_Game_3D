def draw_hud():

    glColor3f(1, 1, 1)

    draw_text(10, window_height - 30, f"Health: {health}")
    draw_text(10, window_height - 60, f"Score: {score}")
    draw_text(10, window_height - 90, f"Lives: {lives}")
    draw_text(10, window_height - 120, f"Enemies: {len(enemies)}")