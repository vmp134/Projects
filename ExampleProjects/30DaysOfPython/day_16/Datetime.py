from datetime import datetime

#1
Current = datetime.now()

#2
print(Current.strftime("%m/%d/%Y, %H:%M:%S"))

#3
newTime = datetime.strptime("5 December, 2019", "%d %B, %Y")

#4
newYear = datetime(2026,1,1)
difference1 = newYear - Current

#5
oldYear = datetime(1970,1,1)
difference2 = Current - oldYear

#6
'''
Probably for datapoints on a graph to find the change over time
'''
