from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.car_box = []
        self.generate_new_car()

    def generate_new_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(320, random.randint(-230, 250))
            self.car_box.append(new_car)

    def remove_old_car(self):
        self.car_box.pop(0)

    def move(self):
        for car in self.car_box:
            car.goto(car.xcor() - self.move_distance, car.ycor())

    def increase_move_distance(self):
        self.move_distance += MOVE_INCREMENT
