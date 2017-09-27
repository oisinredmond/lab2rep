myList = [49,13,100,19,67,12,55,89,2,34]

max = 0

for i in range(0,len(myList)):
  if myList[i] > max:
    max = myList[i]

print "Max number in list: " + str(max)
