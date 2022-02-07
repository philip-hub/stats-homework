from pandas import *


data = read_csv("EXR_C02_S03_07.csv") #this can and should be changed depending on the problem

list2 = data['SCORES'].tolist()

list2 = sorted(list2) #as an ordered array
print("\nOrdered Array\n") 
print(str(list2)+"\n") #displays ordered array

print("Mean\n")

listNum=0 # number of values in the list
meanSum=0 # the total summation 

for i in list2:
  meanSum = i + meanSum # find the total sum
  listNum = listNum+1 # find the total number of values in the list

print("Number of Data Points: "+str(listNum))
mean = meanSum/listNum # find the mean
print("Mean : "+str(mean))


print("Varience\n")
sumVarience =0 
for value in list2:

  t = value - mean # (xi - mean)
  t = t**2
  print(str(value)+" : "+str(t))
  sumVarience = t+sumVarience



samDem = listNum-1
varience = sumVarience/samDem
std = varience**.5
range_ =  (list2[listNum-1] - list2[0])

print("\nTotal Varience sum : "+str(sumVarience))
print("Varience: "+str(varience))
print("STD: "+str(std))
print("Range :"+str(range_))
