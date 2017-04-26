#!/usr/bin/python

## This program is a simulation of a block/ball moving along a surface of a chosen material.
## It will show the effects of choosing materials with different coefficients of friction.
## The idea is that the user will enter a choice of material for the surface of the bottom
## of the window and a speed for the block/ball. Based on the choice of surface and the
## resulting coefficient of friction, the block/ball will move until eventually it will stop
## as the frictional force will have slowed all of the momentum of the block/ball.



from graphics import *

gravity = 9.8  #meters per second per second

def main():
    win = GraphWin()
    coefficient = get_materials()
    speed = get_initial_speed()
    begin_motion(coefficient, speed, mass)
    display_message()


def begin_motion(coefficient, speed, mass):
    frictional_acceleration = coefficient * gravity    


main()
