from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    global dir
    global z
    global x

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                z = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                z = 0
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                z = 3
            elif event.key == SDLK_LEFT:
                dir += 1
                z = 2


running = True
x = 800 / 2
frame = 0
dir = 0
z = 0

while running:
    clear_canvas()
    grass.draw(400, 30)

    character.clip_draw(frame * 100, z * 100, 100, 100, x, 90)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if 780 > x > 20:
        x += dir
    elif x == 780:
        x -= 1
    elif x == 20:
        x += 1

close_canvas()
