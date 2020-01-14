temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
hours=["12 Am","1 Am","2 AM","3 AM","4 AM","5 AM","6 AM","7 AM","8 AM","9 AM","10 AM","11 AM","12 PM"," 1 PM"," 2 PM"," 3 PM"," 4 PM"," 5 PM"," 6 PM"," 7 PM"," 8 PM"," 9 PM"," 10 PM"," 11 PM"]

maximum_temperature=max(temperatures_C)
minimum_temperature=min(temperatures_C)
print("the minimum temperature is = %d" %minimum_temperature)
print("the maximum temperature is = %d" %maximum_temperature)

t1 = 70 # Set point temperature
t2 = [i for i in temperatures_C if i > t1]
print("temperatures greater than 70= ", t2)

#mean
mean_temperature=sum(temperatures_C)/len(temperatures_C)
print("The average temperature during the day was =%d" % mean_temperature)
temperature_3am= (int((temperatures_C[2] + temperatures_C[4])/ 2))
print("temperature at 3am= %d" % temperature_3am ,"C" )
temperatures_C[3] = temperature_3am
print("New list with 3 am temperature updated = ", temperatures_C)


#temperatures_F= (((1.8  * i) + 32) for i in (temperatures_C))
temperatures_F = [((i * 1.8) + 32 ) for i in temperatures_C]

#temperatures_F= [ '%.2f' % elem for elem in (temperatures_F)]
print("Temperatures in F: " ,temperatures_F)
#Average temperatures
average_temperature_C=sum(temperatures_C)/len(temperatures_C)
print("The average temperature in C =%.2f" %average_temperature_C)

average_temperature_F=sum(temperatures_F)/len(temperatures_F)
print("The average temperature in F =%d" % average_temperature_F)

# Standard Deviation
import statistics as stats

standard_deviation_C= (stats.stdev(temperatures_C))
print("Standard deviation in C= %.2f" % standard_deviation_C)

standard_deviation_F= (stats.stdev(temperatures_F))
print("Standard deviation in F= %.2f" % standard_deviation_F)
#Solving problem
count = 0
hight_temperature=80
for i in temperatures_C:
    if i >= t1:
        count = count + 1
if count > 4:
    print("Cooling system must be changed ")
elif all(value > hight_temperature for value in temperatures_C):
    print("Cooling system must be changed ")
elif mean_temperature > 65:
    print(" Cooling system must be changed ")
else:
    print("Cooling system working fine")

#future improvements

temperatures_recorded = {hours[i]: temperatures_C[i] for i in range(len(hours))}
#print("Temperature/time:", temperatures_recorded)


for hours,temperatures_C in temperatures_recorded.items():
    if temperatures_C > t1:
        print("Temperature over 70 at :" , hours)

failure=0
good=0
for t80 in range(temperatures_C):
        if t80 > 80:
            failure += 1
            good = 0
            if failure == 3:
                print("Colling unit must be replaced")
        elif t80 < 80:
            good+=1
            failure = 0
            if good == 3:
                print("Colling unit working under parameters")
        elif t80 > 80:
            print("Colling unit must be replaced")
        elif average_temperature_C > 65:
            print("Colling Unit must be replaced")
        else:
            print("Colling unit working under parameters")



