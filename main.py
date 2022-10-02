import turtle
import random

arena_speed = 10
step = 30
start = False


def MainLooping():
    while True:
        MapLooping(arena, arena, enemy, enemy2)
    wd.ontimer(MapLooping, 60 // 1000)



def PlayerInitial(turtle_player):
    turtle_player.goto(0, -300)


def RandomPos(obj_turtle):
    obj_turtle.goto(random.randint(-200, 200), 400)


def WalkRight():
    if player.xcor() < 245 and player.xcor() + step < 245:
        player.forward(step)
    else:
        PlayerInitial(player)


def WalkLeft():
    if player.xcor() > -230 and player.xcor() - step > -230:
        player.backward(step)
    else:
        PlayerInitial(player)


def ObjDown(obj_turtle):
    if obj_turtle.ycor() < -600:
        obj_turtle.pen(shown=False, pensize=2, speed=0)
        obj_turtle.goto(random.randint(-200, 200), 400)

    if CollisionObj(obj_turtle, player, 25, 30):
        PlayerInitial(player)

    obj_turtle.fd(step)


def Enemies(turtle_enemies):
    turtle_enemies.pen(shown=True, pendown=False, speed=2)
    turtle_enemies.shape("img/player.gif")
    turtle_enemies.setheading(270)
    ObjDown(turtle_enemies)


def MapLooping(arena_static, arena_movement, enemy_map, enemy_map2):
    arena_static.setpos(arena.xcor(), arena.ycor() - 15)
    arena_movement.setpos(arena.xcor(), arena.ycor() - 15)
    Enemies(enemy_map)
    Enemies(enemy_map2)
    if arena_movement.ycor() < -800:
        arena_movement.speed(0)
        arena_movement.setpos(0, 80)
        arena_movement.speed(arena_speed)


def CollisionObj(obj_one, obj_two, margin_x, margin_y):
    if (obj_one.xcor() <= obj_two.xcor() + margin_x) and (obj_one.xcor() >= obj_two.xcor() - margin_x) and (obj_one.ycor() <= obj_two.ycor() + margin_y):
        print("colidiu")
        return True


wd = turtle.Screen()
wd.title('Ultra Surf')
wd.setup(width=1000, height=800, starty=0)
wd.addshape("img/background.gif")
wd.addshape("img/player.gif")

arena = turtle.Turtle()
arena.shape('img/background.gif')
arena.speed(arena_speed)
arena.up()

player = turtle.Turtle()
player.shape("img/player.gif")
player.up()
PlayerInitial(player)


wd.onkey(WalkRight, 'Right')
wd.onkey(WalkLeft, 'Left')
wd.listen()

enemy = turtle.Turtle()
enemy.pen(shown=False, pendown=False)
RandomPos(enemy)

enemy2 = turtle.Turtle()
enemy2.pen(shown=False, pendown=False)
RandomPos(enemy2)

MainLooping()
wd.mainloop()