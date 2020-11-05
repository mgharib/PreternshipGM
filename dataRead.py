#imports our created LinkedList class
import LinkedList

#initializes list of CSV files
datfile = list()

#adds the CSV files to the list
datfile.append('Example1.csv')
datfile.append('Example2.csv')
datfile.append('Example3.csv')

#creates linked list 
valueList = LinkedList.LinkedList()

#loops through all the files
for fh in datfile:
	#opens the file and reads in data
	f = open(fh, 'r')

	#goes through each line
	for line in f:
		#sets values equal to an array of each variable in the line
		values = line.split(',')
	#	if (values[0] == whatever): // will make sure only desired values are added
		#adds value to linked list
		valueList.add_first(LinkedList.Node(values[2]))
	f.close()

#prints out the linked list to make sure it is correct
print(valueList)
