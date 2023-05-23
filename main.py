import turtle
import time
import random
import threading

tosbaga = turtle.Screen()
tosbaga.bgcolor("light blue")
tosbaga.title("Tosbağa Ödevi")


score = 0
sayac_turtle = turtle.Turtle()
random_turtle = turtle.Turtle()
skor = turtle.Turtle()
game_ower = turtle.Turtle()

skor.hideturtle()
skor.color("red")
skor.penup()
skor.goto(0, 250)


sayac_turtle.hideturtle()
sayac_turtle.color("blue")
sayac_turtle.penup()
sayac_turtle.goto(0, 300)

random_turtle.hideturtle()
random_turtle.shapesize(2)
random_turtle.color("green")
random_turtle.shape("turtle")
random_turtle.penup()

game_ower.hideturtle()
game_ower.color("purple")
game_ower.penup()
game_ower.goto(0, -300)

def sayac(sayi):
    global random_turtle
    while sayi >= 0:
        sayac_turtle.clear()
        sayac_turtle.write(f'SAYAÇ: {sayi}', align="center", font=("Courier", 30, "normal"))
        sayi -= 1
        time.sleep(1)
        random_turtle.showturtle()
        time.sleep(0.25)
        random_turtle.hideturtle()

        x = random.randint(-350, 250)
        y = random.randint(-350, 250)
        random_turtle.goto(x, y)

        if sayi < 0:
            game_ower.write('GAME OWER', align="center", font=("Courier", 30, "normal"))




def Score():
    skor.clear()
    skor.write(f'SCORE: {score}', align="center", font=("Courier", 30, "normal"))


def turtle_click(x, y):
    global score, random_turtle
    if random_turtle.distance(x, y) < 30:
        score += 1
        Score()



def main():
    threading.Thread(target=sayac, args=(30,)).start()
    turtle.onscreenclick(turtle_click)
    Score()
    turtle.mainloop()


main()