#Hard, i had no idea how to do it so i had to use information from stackoverflow.

import random

random.seed(10)
def generate_random_point():

    #start at 0.0, r=1 so it will be between -1 and 1
    return random.uniform(-1,1), random.uniform(-1,1)

def is_in_unit_circle(p1):
    return p1[0] ** 2 + p1[1] **2 <=1

def estimate(x):
    points_in_circle = 0

    for i in range(x):
        point = generate_random_point()

        if is_in_unit_circle(point):
            points_in_circle+=1

    result = 4 * points_in_circle/x
    return result