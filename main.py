import turtle
import random

stamina = 100
velocity = 0
score = 0
step = 10


def MainLooping():
    global stamina, score, velocity
    score_pen.clear()
    stamina_pen.clear()

    MapLooping(arena)
    if velocity != 0:
        ObjDown(obstacle1)
        ObjDown(obstacle2)
        score += 10
        stamina -= 1

    if stamina == 0:
        velocity = 0
        stamina = 100
        print("Acabou a gasosa =(")

    WriteScreen(score_pen, f"Pontuação {score}")
    WriteScreen(stamina_pen, f"Energia: {stamina}")

    wd.update()
    wd.ontimer(MainLooping, 1000 // 60)


def MapLooping(scenery):
    scenery.setpos(scenery.xcor(), scenery.ycor() - velocity)
    if scenery.ycor() < -800:
        scenery.speed(0)
        scenery.setpos(0, scenery.ycor() + 700)
        scenery.speed(10)


def ObjDown(obj_turtle):
    global velocity

    if obj_turtle.ycor() < -600:
        RandomPos(obj_turtle)

    if CollisionPlayer(obstacle1, 85, 90, 0, 0):
        PlayerInitial()
        velocity = 0 #Controla a velocidade do jogo

    obj_turtle.fd(step)


def CollisionPlayer(obj, margin_left, margin_right, margin_up, margin_down):
    if (player.xcor() - 45 <= obj.xcor() + margin_right) and (player.xcor() + 75 >= obj.xcor() - margin_left):
        if -230 >= obj.ycor() >= -300:
            print("KABUUUUUUUUUM")
            return True


def Start():
    global velocity
    velocity = 15


def RandomPos(obj_turtle):
    obj_turtle.goto(random.randint(-190, 190), random.randint(400, 700))


def PlayerInitial():
    player.goto(0, -300)


def WalkRight():
    if player.xcor() < 245 and player.xcor() + step < 245:
        player.forward(step)
    else:
        PlayerInitial()


def WalkLeft():
    if player.xcor() > -230 and player.xcor() - step > -230:
        player.backward(step)
    else:
        PlayerInitial()


def Enemies(turtle_enemies):
    turtle_enemies.pen(shown=True, pendown=False, speed=2)
    turtle_enemies.shape("img/obstacle.gif")
    turtle_enemies.setheading(270)


def WriteScreen(pen, text):
    pen.write(text, align="center", font=("Times", 18, "bold"))


def PenWrite(obj, x, y):
    obj.hideturtle()
    obj.up()
    obj.goto(x, y)


#Configuração da Janela
wd = turtle.Screen()
wd.title('Barquinho do Balocubaco')
wd.setup(width=1000, height=800, starty=0)
wd.addshape("img/background.gif")
wd.addshape("img/player.gif")
wd.addshape("img/obstacle.gif")

#Cenário
arena = turtle.Turtle()
arena.shape('img/background.gif')
arena.speed(10)
arena.up()

#Jogador
player = turtle.Turtle()
player.shape("img/player.gif")
player.up()
PlayerInitial()

#Obstaculos
obstacle1 = turtle.Turtle()
obstacle1.pen(shown=False, pendown=False)
RandomPos(obstacle1)
Enemies(obstacle1)

obstacle2 = turtle.Turtle()
obstacle2.pen(shown=False, pendown=False)
RandomPos(obstacle2)
Enemies(obstacle2)

#Pontuação
score_pen = turtle.Turtle()
PenWrite(score_pen, 400, 300)

#Energia
stamina_pen = turtle.Turtle()
PenWrite(stamina_pen, -400, 300)

#Chamada das funções
wd.onkeypress(WalkRight, 'Right')
wd.onkeypress(WalkLeft, 'Left')
wd.onkey(Start, "space")
wd.listen()
wd.tracer(0)

MainLooping()
wd.mainloop()