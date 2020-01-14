import statistics as stats

def main():
    stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]
    bus_stops=len(stops)
    print("Total Bus Stops:", bus_stops)
    bus_occupation = 0
    bus_stop=[]

    for x,y in stops:
        bus_in= x
        bus_out= y
        buss_flow = (int(x) - int(y))
        bus_occupation = bus_occupation + buss_flow
        bus_stop.append(bus_occupation)
    max_bus_occupation=max(bus_stop)
    print("Max Bus Occupation:",max_bus_occupation)
    average_bus_occupation = sum(bus_stop) / len(bus_stop)
    print("Average Occupation per stop:", round(average_bus_occupation))
    standard_deviation_bus_occupation = (stats.stdev(bus_stop))
    print("Standard deviation in Bus occupation= %.2f" % standard_deviation_bus_occupation)


if __name__ == '__main__':
    main()



