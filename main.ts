let EmptyObstacleY = 0
let ticks = 0
let obstacle : game.LedSprite[] = []
let Bird : game.LedSprite = null
let rockets : game.LedSprite[] = []
Bird = game.createSprite(0, 2)
Bird.set(LedSpriteProperty.Blink, 300)
function launch_rocket() {
    
    let rocket = game.createSprite(1, Bird.get(LedSpriteProperty.Y))
    rockets.push(rocket)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    Bird.change(LedSpriteProperty.Y, -1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    launch_rocket()
})
function check_gameover() {
    for (let obstacle3 of obstacle) {
        if (obstacle3.get(LedSpriteProperty.X) == Bird.get(LedSpriteProperty.X) && obstacle3.get(LedSpriteProperty.Y) == Bird.get(LedSpriteProperty.Y)) {
            game.gameOver()
        }
        
    }
}

function check_rocket_collision() {
    let rocketx: number;
    let rockety: number;
    let obstacleX: number;
    let obstacleY: number;
    for (let rocket of rockets) {
        for (let obstacle3 of obstacle) {
            rocketx = rocket.get(LedSpriteProperty.X)
            rockety = rocket.get(LedSpriteProperty.Y)
            obstacleX = obstacle3.get(LedSpriteProperty.X)
            obstacleY = obstacle3.get(LedSpriteProperty.Y)
            if (rocketx == obstacleX && rockety == obstacleY) {
                obstacle.removeElement(obstacle3)
                obstacle3.delete()
                rockets.removeElement(rocket)
                rocket.delete()
            }
            
        }
    }
}

basic.forever(function on_forever() {
    
    while (obstacle.length > 0 && obstacle[0].get(LedSpriteProperty.X) == 0) {
        obstacle.removeAt(0).delete()
    }
    for (let obstacle2 of obstacle) {
        obstacle2.change(LedSpriteProperty.X, -1)
    }
    check_rocket_collision()
    for (let rocket of rockets) {
        rocket.change(LedSpriteProperty.X, 1)
    }
    check_rocket_collision()
    check_gameover()
    game.setScore(game.score() + 1)
    basic.pause(300 - ticks * 10)
    Bird.change(LedSpriteProperty.Y, 1)
    check_gameover()
    if (ticks % 3 == 0) {
        EmptyObstacleY = randint(0, 4)
        for (let index = 0; index < 5; index++) {
            if (index != EmptyObstacleY) {
                obstacle.push(game.createSprite(4, index))
            }
            
        }
    }
    
    ticks += 1
    basic.pause(300 - ticks * 10)
})
