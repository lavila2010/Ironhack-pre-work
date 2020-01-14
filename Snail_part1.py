print("--------The Snail and the Well Part 1----------")

def main():
    well_height= 125
    daily_average= 30
    night_retreat= 20
    climbed_distance=daily_average-night_retreat
    snail_position=0
    days = []

    while snail_position < well_height:
        snail_position+= climbed_distance
        days.append(snail_position)

    print("Days taken to climb the well:", len(days))

if __name__ == '__main__':
    main()

# Bonus part

import statistics as stats

print("----------Snail bonus part-------------")
def main():
    well_height=125
    advance_cm = [30,21,33,77,44,45,23,45,12,3,55]
    night_retreat=20
    daily_advance = [i-night_retreat for i in advance_cm]
    print("Daily snail advance:", daily_advance)
    count=0

    for i in daily_advance:
        if i < well_height:
            count= count + i

    print("Days taken to climb the well=",count)
    #maximum displacement in a day
    maximum_displacement=max(daily_advance)
    print("Maximmum displacement in a day was:", maximum_displacement)
    #maximum displacement in a day
    minimum_displacement=min(daily_advance)
    print("Minimum displacement in a day was ", minimum_displacement)
    #Average Progress
    average_progress= sum(daily_advance)/len(daily_advance)
    print("Average distance climbed in a day:%.2f" %average_progress)
    # Standard Deviation

    standard_deviation= (stats.stdev(advance_cm))
    print("The standard deviation of displacament during the day was %.2f:" % standard_deviation)

if __name__ == '__main__':
    main()