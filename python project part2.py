start = int(input("Enter start year: "))
end = int(input("Enter end year: "))

while start >= end:
    print("Check your year input again.")
    start = int(input("Enter start year: "))
    end = int(input("Enter end year: "))

print ("Here is a list of leap years between {0} and {1}:".format(start,end))

leap_years = []
while start <= end:
    if start % 4 == 0 and start % 100 != 0:
        leap_years.append(str(start))
    if start % 100 == 0 and start % 400 == 0:
        leap_years.append(str(start))
    start += 1

for line in range(0, len(leap_years), 10):
    print ("{0}.".format(", ".join(leap_years[line:line+10])))

while start >= end:
    print("Check your year input again.")
    start = int(input("Enter start year: "))
    end = int(input("Enter end year: "))


print ("Here is a list of non_leap years between {0} and {1}:".format(start,end))


non_leapyears=[]
while start<=end:
    if start%4!=0 and start%100 !=0 and start%400 != 0:
        non_leapyears.append(str(start))
    start += 1

for line in range(0, len(non_leapyears), 10):
    print ("{0}.".format(", ".join(non_leapyears[line:line+10])))


        
