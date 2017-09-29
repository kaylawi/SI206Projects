import os
import filecmp
import csv
from operator import itemgetter
from collections import Counter
from datetime import date

def getData(file):
    somelist = []
    with open(file, "r") as somefile:
        
        file_holder = csv.DictReader(somefile)
    
        for row in file_holder:

            tempdictionary = {}
            
            tempdictionary["First"] = row["First"]
            tempdictionary["Last"] = row["Last"]
            tempdictionary["Email"] = row["Email"]
            tempdictionary["Class"] = row["Class"]
            tempdictionary["DOB"] = row["DOB"]

            somelist.append(row)

    return somelist

# TASK TWO

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

    value = sorted(data, key= itemgetter(col))
    return value[0]["First"] + " " + value[0]["Last"]


# TASK THREE

#Create a histogram
def classSizes(data):
  
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

    c = Counter()
    
    for size in data:
        
        c[size["Class"]] += 1

    return c.most_common()

#TASK FOUR

# Find the most common day of the year to be born

def findDay(a):
## Input: list of dictionaries
## Output: Return the day of month (1-31) that is the
## most often seen in the DOB

    day_dic = {}
    for value in a:
        birthday = value['DOB']
        day = birthday.split('/')
        day_num = day[1]
      

        if day_num not in day_dic:
            day_dic[day_num] = 1
        else:
            day_dic[day_num] +=1
              

    listday = list(day_dic.items())
    listday = sorted(listday, key = lambda x: x[1], reverse = True)
    return int(listday[0][0])

#TASK FIVE

# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

month_dic = {}

    today_date = date.today()
    year_today = today_date.year
    month_today = today_date.month
        
    #Month
    
        if month_num not in month_dic:
            month_dic[month_num] = 1
        else:
            month_dic[month_num] +=1
                
    listmonth = list(month_dic.items())
    listmonth = sorted(listmonth, key = lambda x: x[0], reverse = True)
    return int(listmonth[0][0])
    
    #Year
    
    if year_num not in year_dic:
        year_dic[year_num] = 1
        else:
            year_dic[year_num] +=1

    listmonth = list(year_dic.items())
    listmonth = sorted(listyear, key = lambda x: x[2], reverse = True)
    return int(listmonth[0][0])


#TASK SIX

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

    with open('fileName','wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter= ',', quotechar='|',
                            quoting= csv.QUOTE_MINIMAL)

        filewriter.writerow(["First"])
        filewriter.writerow(["Last"])
        filewriter.writerow(["Class"])
        filewriter.writerow(["DOB"])


                        





################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
