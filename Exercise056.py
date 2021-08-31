import random

random.seed(20)
def generate_random_point():

    #start at 0.0, r=1 so it will be between -1 and 1
    return random.uniform(-1,1), random.uniform(-1,1)

def is_in_unit_circle(p1):
    return p1[0] ** 2 + p1[1] **2 <=1

points = [generate_random_point() for i in range(15)]
flags = [is_in_unit_circle(point) for point in points]
print(flags)