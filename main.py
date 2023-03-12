import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

car_spawn_time = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    if car_spawn_time == 0:
        car_manager.add_car()
        car_spawn_time = 6
    car_spawn_time -= 1

    car_manager.move_cars()
    screen.update()

    # detect collision with car and delete cars, that have passed the left screen border
    for car in car_manager.car_list:
        if car.xcor() < -300:
            car_manager.remove_car(car_manager.car_list.index(car))
        if abs(player.xcor() - car.xcor()) < 30 and abs(player.ycor() - car.ycor()) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect reaching top edge by the player
    if player.ycor() > FINISH_LINE_Y:
        player.reset_pos()
        car_manager.difficulty += 1
        scoreboard.update_score()

screen.exitonclick()