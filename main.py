def on_button_pressed_a():
    Bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Bird.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

EmptyObstacleY = 0
Bird: game.LedSprite = None
ticks = 0
obstacle: List[game.LedSprite] = []
Bird = game.create_sprite(0, 2)
Bird.set(LedSpriteProperty.BLINK, 300)

def on_forever():
    global EmptyObstacleY, ticks
    while len(obstacle) > 0 and obstacle[0].get(LedSpriteProperty.X) == 0:
        obstacle.remove_at(0).delete()
    for obstacle2 in obstacle:
        obstacle2.change(LedSpriteProperty.X, -1)
    if ticks % 3 == 0:
        EmptyObstacleY = randint(0, 4)
        for index in range(5):
            if index != EmptyObstacleY:
                obstacle.append(game.create_sprite(4, index))
    for obstacle3 in obstacle:
        if obstacle3.get(LedSpriteProperty.X) == Bird.get(LedSpriteProperty.X) and obstacle3.get(LedSpriteProperty.Y) == Bird.get(LedSpriteProperty.Y):
            game.game_over()
    ticks += 1
    basic.pause(1000)
basic.forever(on_forever)

