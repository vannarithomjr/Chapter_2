#makes sure after a space there is a comma when it prints
# print("one", "two", "three", sep=", ")

#print "Hello World!" in a single line
# print("Hello", end=" ") #\r
# print("World!")

#Learning how to use tab and new line
#print("a\tb\tc") #a     b      c
#print("a\tb\tc\nd\te\tf") #this one is going to be very similar but a new line is going to start with letter d


#print("\"Hello World!\"") #This is the way to include the quotation

#This is the way to mke tables like in Excel
# print("0123456789012345678901234567")
# print("Rank".ljust(5), "Player".ljust(20), "HR".rjust(3), sep="")
# print('1'.center(5), "Barry Bonds".ljust(20), "762".rjust(3), sep="")
# print('2'.center(5), "Hank Aaron".ljust(20), "755".rjust(3), sep="")
# print('3'.center(5), "Babe Ruth".ljust(20), "714".rjust(3), sep="")

#This is the way to manipulate at the end the input of the string with the format method
# print("There are {0}% probability that the stock market will crash tomorrow and {1}% probability that it will rally!".format(10, 50))

#This is another way to do exactly the same thing than above but in two steps
# str1 = "There are {0}% probability that the stock market will crash tomorrow and {1}% probability that it will rally!"
# print(str1.format(10, 50))


#Justufication output format using the same table previusly used
# print("0123456789012345678901234567")
# print("{0:^5s}{1:<20s} {2:>3s}".format("Rank", "Player", "HR"))
# print("{0:^5n}{1:<20s} {2:>3n}".format(1, "Barry Bonds", 762))
# print("{0:^5n}{1:<20s} {2:>3n}".format(2, "Hank Aaron", 755))
# print("{0:^5n} {1:<20s} {2:>3n}".format(3, "Babe Ruth", 714))

#Demonstrate use of the format method.
print("The area of {0:s} is {1:,d} square miles.".format("Texas", 268820))
str1 = "The population of {0:s} is {1:.2%} of the U.S. population."
print(str1.format("Texas", 26448000/309000000))