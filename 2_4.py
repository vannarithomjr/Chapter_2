#Demonstrating how ineficient in terms of time multimple variables are
# num1 = 1
# num2 = 10
# num3 = 1000
# sum_of_all_numbers = num1 + num2 + num3
# print("The sum is {0:n}".format(sum_of_all_numbers))



#Lists or arrays are better because we don't need to give a name to the variable of each number
list_of_numbers = [1, 10, 1000]
# print("The sum is", sum(list_of_numbers))
print (list_of_numbers) # [1, 10, 100]

list_of_numbers = [] # sets the list to an empty list
print(list_of_numbers) # []

list_of_numbers.append(100) # adds the member to the end of the list
print(list_of_numbers) # [100]

# add 100 four times to the list
list_of_numbers.append(100)
list_of_numbers.append(100)
list_of_numbers.append(100)
list_of_numbers.append(100)
print(list_of_numbers) # [100, 100, 100, 100, 100]

list_of_numbers_2 = [3, 100, 5] # new list with different members
print(list_of_numbers_2) # [3, 100, 5]

list_of_numbers.extend(list_of_numbers_2) # merges both lists together (the list 2 at the end)
print(list_of_numbers)

l1 = [1, 32, 4]
l2 = [100, 200, 300]
l3  = l1 + l2 # merges both lists just as the extend() function
print(l3)

words = ["Spam", "Wink", "Hi"]
words.insert(len(words), "Hello") # insterts the word in the specified index. since len() evaluates the number of items in a list, the index is the last member
print("words========>", words)

print([0] * 3) # list repetition


# Program requests five grades as input, 
# displays average after dropping two lowest grades
#Calculate average of grades
grades = []
num = float(input("Enter the first grade: "))
grades.append(num)
num = float(input("Enter the second grade: "))
grades.append(num)
num = float(input("Enter the third grade: "))
grades.append(num)
num = float(input("Enter the fourth grade: "))
grades.append(num)
num = float(input("Enter the fifth grade: "))
grades.append(num)
minimumGrade = min(grades)
print("The minimum Grade is:", minimumGrade)
grades.remove(minimumGrade)
print("Now the list looks like this:", grades)
minimumGrade = min(grades)
print("The minimum Grade is:",minimumGrade)
grades.remove(minimumGrade)
print("Now the list looks like this:", grades)
average = sum(grades) / len(grades)
print("Average Grade: {0:.2f}".format(average))