EmptyObstacleY = 0
ticks = 0
obstacle: List[game.LedSprite] = []
Bird: game.LedSprite = None
rockets: List[game.LedSprite] = []
Bird = game.create_sprite(0, 2)
Bird.set(LedSpriteProperty.BLINK, 300)

def launch_rocket():
    global rockets
    rocket = game.create_sprite(1, Bird.get(LedSpriteProperty.Y))
    rockets.push(rocket)

def on_button_pressed_a():
    Bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    launch_rocket()
input.on_button_pressed(Button.B, on_button_pressed_b)

def check_gameover():
    for obstacle3 in obstacle:
        if obstacle3.get(LedSpriteProperty.X) == Bird.get(LedSpriteProperty.X) and obstacle3.get(LedSpriteProperty.Y) == Bird.get(LedSpriteProperty.Y):
            game.game_over()

def check_rocket_collision():
    for rocket in rockets:
        for obstacle3 in obstacle:
            rocketx = rocket.get(LedSpriteProperty.X)
            rockety = rocket.get(LedSpriteProperty.Y)
            obstacleX = obstacle3.get(LedSpriteProperty.X)
            obstacleY = obstacle3.get(LedSpriteProperty.Y)
            if rocketx == obstacleX and rockety == obstacleY:
                obstacle.remove_element(obstacle3)
                obstacle3.delete()
                rockets.remove_element(rocket)
                rocket.delete()

def on_forever():
    global EmptyObstacleY, ticks
    while len(obstacle) > 0 and obstacle[0].get(LedSpriteProperty.X) == 0:
        obstacle.remove_at(0).delete()

    for obstacle2 in obstacle:
        obstacle2.change(LedSpriteProperty.X, -1)

    check_rocket_collision()

    for rocket in rockets: 
        rocket.change(LedSpriteProperty.X, 1)

    check_rocket_collision()
    check_gameover()

    game.set_score(game.score() + 1)
    
    basic.pause(300 - ticks * 10)

    Bird.change(LedSpriteProperty.Y, 1)

    check_gameover()

    if ticks % 3 == 0:
        EmptyObstacleY = randint(0, 4)
        for index in range(5):
            if index != EmptyObstacleY:
                obstacle.append(game.create_sprite(4, index))

    ticks += 1

    basic.pause(300 - ticks * 10)


basic.forever(on_forever)
