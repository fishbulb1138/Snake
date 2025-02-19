from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME!")

def create_segment():
    segment = Turtle("square")
    segment.penup()
    segment.color("white")
    return segment



starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    seg = create_segment()
    seg.goto(position)
    segments.append(seg)

game_is_active = True

while game_is_active:
    for seg in segments:
        seg.forward(20)









screen.exitonclick()
