import math

def main():
    points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
              (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]
    arrows = set(points)
    print("Arrows set:", arrows)
    print("Arrows shot by Robin Hood:", len(arrows))
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    target=0

    for x,y in arrows:
        if x in range(0,9) and y in range(0,9):
            q1+=1
        elif x in range(0,9) and y in range(-9,0):
            q2+=1
        elif x in range(-9,0) and y in range(-9,0):
            q3+=1
        elif x in range(-9,0) and y in range(0,9):
            q4+=1
        elif (x==0) and (y==0):
            target+=1
        else:
            print("")
    print("Arrows in quadrant N1:", q1)
    print("Arrows in quadrant N2:", q2)
    print("Arrows in quadrant N3:", q3)
    print("Arrows in quadrant N4:", q4)
    print("Robin Hood hit the target N times:", target,)

    min_point = []
    for i in range(len(points)):
        min_point.append(math.sqrt(points[i][0] ** 2 + points[i][1] ** 2))
    print("Min distance is:", min(min_point), "Point: ", points[min_point.index(min(min_point))])

    rad_9 = [(points[i][0], points[i][1]) for i in range(len(points)) if abs(points[i][0]) > 9 or abs(points[i][1]) > 9]
    print("Arrows out radius = 9 :", rad_9)

if __name__ == '__main__':
    main()