#This mini program takes a full name and recognizes the first name and the last name.
#full_name = input("Enter your full name:")
#index_of_space = full_name.rfind(" ")
#first_name = full_name[:index_of_space]
#last_name = full_name[index_of_space+1:]
#print("First name:", first_name)
#print("Last name:", last_name)

#This mini program calculates the monthly income given the annual income
#annual_income = eval(input("Enter your annual income: "))
#print("User's income is ", annual_income)
#monthly_income = annual_income/12
#print("monthly income is", monthly_income)

str1 = "Python"
length = len(str1) # is equal to a int 5

str2 = str1[:] # is equal to a string Python 
print("str2 :", str2)
str3 = str1[:10] # this is an error because there is not index 10 in this specific string
print("str3 : ", str3)
str4 = str2[2:-1]
print("str4 :", str4)
