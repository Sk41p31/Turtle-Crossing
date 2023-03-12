from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list = []
        self.difficulty = 0

    def add_car(self):
        new_car = Car(self.difficulty)
        self.car_list.append(new_car)

    def remove_car(self, index):
        self.car_list[index].ht()
        self.car_list.pop(index)

    def clear_cars(self):
        self.car_list.clear()

    def move_cars(self):
        for car in self.car_list:
            car.move()


class Car(Turtle):

    def __init__(self, speed_level):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.speed_level = speed_level

        self.seth(180)
        self.penup()
        self.goto(300, random.randint(-230,230))

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE + self.speed_level * MOVE_INCREMENT)
