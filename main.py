import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # remove old car to free memory
    if len(car_manager.car_box) > 0:
        if car_manager.car_box[0].xcor() <= -320:
            car_manager.remove_old_car()

    # detect collision with car
    for index in range(len(car_manager.car_box)):
        cur_car = car_manager.car_box[index]
        if cur_car.distance(player) <= 20:
            score.game_over()
            game_is_on = False
            break

    # detect finish level
    if player.pass_level():
        player.refresh()
        car_manager.increase_move_distance()
        score.increase_level()
        score.update()

    car_manager.generate_new_car()
    car_manager.move()

screen.exitonclick()
