##importing library functions
import random
import math

##class to define 2 points x and y for the plane
class twoPoints:
    def __init__(self, x, y):
        self.x = x
        self.y = y

##Sorting the array based on the x and y coordinates and finding the distance
def distance_x_y(a, b): #considering a and b are 2 points
    X = a.x - b.x
    Y = a.y - b.y
    return math.sqrt(X * X + Y * Y)

##Function to find the shortest distance between X and Y
def shortestDistance_two_points(p, v1, v2):
    minimum_distance = float("inf") #infinity - if the quantity is larger than finite number
    for g in range(v1, v2):
        for h in range(g + 1, v2):
            distance = distance_x_y(p[g], p[h])
            if distance < minimum_distance:
                minimum_distance = distance
    return minimum_distance

##Function to find the closest pair of points in the delta region
def closest_pair_of_points(p, dl, dr): #p - point, dl - delta left region, dr - delta right region
    ##checks if the input is lass/equal to 3 (brute force)
    if dr - dl <= 3:
        return shortestDistance_two_points(p, dl, dr)
    mid = (dl + dr) // 2 ##mid point
    mid_point = p[mid]
    left_min_distance = closest_pair_of_points(p, dl, mid) #minimum distance on the left
    right_min_distance = closest_pair_of_points(p, mid, dr) #minimum distance on the right
    min_distance = min(left_min_distance, right_min_distance) #minimum of both the distances
    delta = []
    for g in range(dl, dr + 1):
        if abs(p[g].x - mid_point.x) < min_distance:
            delta.append(p[g])
    delta.sort(key=lambda p1: p1.y)
    ##to find the distance in delta range
    for g in range(len(delta)):
        for h in range(g + 1, len(delta)):
            if delta[h].y - delta[g].y < min_distance:
                dist = distance_x_y(delta[g], delta[h])
                if dist < min_distance:
                    min_distance = dist
    return min_distance

##Function to find the closest pair of points
def closest_pair_main(points):
    p.sort(key=lambda point: point.x)
    return closest_pair_of_points(p, 0, len(p) - 1)

##Main function
if __name__ == "__main__":
    n = 8
    p = [twoPoints(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]
    closest_distance = closest_pair_main(p)
    print(f"The closest pair of random points distance is: {closest_distance}")
